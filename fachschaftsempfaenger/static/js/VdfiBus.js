/*
 * Copyright notice / Urheberrechtshinweis
 *
 * This script is a modified version of "VdfiConnwerk.js" from the website
 * of tüBus (Stadtwerke Tübingen):
 * https://www.tuebus.de/_assets/1ca1c6b546340bc6f2fbefedd326d38e/JavaScript/VdfiConnwerk.js
 *
 * The original code and all rights to it remain with its respective
 * copyright holder(s). This file contains modifications made for the
 * Fachschaftsempfänger project and is not affiliated with, endorsed by,
 * or maintained by the original authors.
 *
 * Dieses Skript ist eine modifizierte Version der Datei "VdfiConnwerk.js"
 * von der Website von tüBus. Der ursprüngliche Code und alle Rechte daran
 * verbleiben bei den jeweiligen Rechteinhabern. Diese Datei enthält
 * Änderungen für das Fachschaftsempfänger-Projekt und steht in keiner
 * Verbindung zu den ursprünglichen Autoren.
 */

function buildDepartureBoardUrl(baseUrl, stopId) {
    const url = new URL(baseUrl, window.location.origin);
    url.searchParams.delete("stop_id");
    url.searchParams.set("stop_id", stopId);
    return url.toString();
}

function departureKey(departure) {
    return [
        departure.line ?? "",
        departure.destination ?? "",
        departure.departure_time ?? "",
        departure.countdown_minutes ?? "",
    ].join("|");
}

function sortDepartures(departures) {
    return departures.slice().sort((a, b) => {
        const ca = Number(a.countdown_minutes);
        const cb = Number(b.countdown_minutes);
        if (!Number.isNaN(ca) && !Number.isNaN(cb) && ca !== cb) {
            return ca - cb;
        }
        const ta = a.departure_time || "";
        const tb = b.departure_time || "";
        return ta.localeCompare(tb);
    });
}

function makeCell(content, strong, asHtml) {
    const td = document.createElement("td");
    let target = td;
    if (strong) {
        target = document.createElement("strong");
        td.appendChild(target);
    }
    if (asHtml) {
        // Only for trusted, locally generated markup (see timeFormat)
        target.innerHTML = content;
    } else {
        target.textContent = content ?? "";
    }
    return td;
}

function renderDepartures(departures, busTableBodyElement, maxDeparturesLength) {
    if (!busTableBodyElement) return;
    const sorted = sortDepartures(departures).slice(0, maxDeparturesLength);
    const rows = [];

    if (sorted.length === 0) {
        const tr = document.createElement("tr");
        const td = document.createElement("td");
        td.colSpan = 3;
        td.className = "bus_status";
        td.textContent = "Keine Verkehrsmittel";
        tr.appendChild(td);
        rows.push(tr);
    }

    sorted.forEach((departure) => {
        const tr = document.createElement("tr");
        if (departure.cancelled === true) tr.className = "cancelled";

        const showPlannedTime = departure.is_realtime === false && departure.departure_time;
        tr.appendChild(showPlannedTime
            ? makeCell(departure.departure_time, true, false)
            : makeCell(timeFormat(departure.countdown_minutes), true, true));
        tr.appendChild(makeCell(lineLabel(departure.line), true, false));
        tr.appendChild(makeCell(departure.destination, false, false));
        rows.push(tr);
    });

    busTableBodyElement.replaceChildren(...rows);
}

function setBusStale(busTableBodyElement, stale) {
    const table = busTableBodyElement?.closest("table");
    if (table) table.classList.toggle("stale", stale);
}

function setBusStatus(busTableBodyElement, text) {
    const row = busTableBodyElement?.querySelector("tr.bus_status_row");
    if (text) {
        if (!row) {
            const tr = document.createElement("tr");
            tr.className = "bus_status_row";
            const td = document.createElement("td");
            td.colSpan = 3;
            td.className = "bus_status";
            td.textContent = text;
            tr.appendChild(td);
            busTableBodyElement.prepend(tr);
        }
    } else if (row) {
        row.remove();
    }
}

const RECONNECT_DELAY_MS = 30000;
let busSource = null;
let busReconnectTimer = null;

// Closes the connection and cancels a pending reconnect.
// Must be called before the tile's DOM is replaced.
function closeVdfiBus() {
    clearTimeout(busReconnectTimer);
    busReconnectTimer = null;
    if (busSource) {
        busSource.close();
        busSource = null;
    }
}

function connectDepartureBoard(baseUrl, stopId, busTableBodyElement, maxDeparturesLength) {
    closeVdfiBus();
    const url = buildDepartureBoardUrl(baseUrl, stopId);
    console.log("vdfi connecting:", url);
    const source = new EventSource(url);
    busSource = source;

    source.addEventListener(
        "open",
        function () {
            setBusStale(busTableBodyElement, false);
            setBusStatus(busTableBodyElement, "");
        },
        false
    );

    source.addEventListener(
        "error",
        function () {
            // EventSource reconnects on its own; until then show data may be outdated
            setBusStale(busTableBodyElement, true);
            busTableBodyElement?.querySelector("tr.bus_loading")?.remove();
            setBusStatus(busTableBodyElement, "Verbindung gestört");

            if (source.readyState === EventSource.CLOSED && busSource === source) {
                clearTimeout(busReconnectTimer);
                busReconnectTimer = setTimeout(() => {
                    connectDepartureBoard(baseUrl, stopId, busTableBodyElement, maxDeparturesLength);
                }, RECONNECT_DELAY_MS);
            }
        },
        false
    );

    source.addEventListener("special_texts", (event) => {
        const specialTextElement = document.getElementById("bus_special_text");
        if (!specialTextElement) return;
        try {
            const data = JSON.parse(event.data);
            const text = Array.isArray(data) && data[0] != null ? String(data[0]).trim() : "";
            // Empty or invalid data clears a previously shown text
            specialTextElement.textContent = text;
        } catch (error) {
            console.error("Error parsing special_texts data:", error);
        }
    });

    source.addEventListener("departures", (event) => {
        try {
            const data = JSON.parse(event.data);
            const merged = new Map();
            if (Array.isArray(data)) {
                data.forEach((departure) => {
                    merged.set(departureKey(departure), departure);
                });
            };
            setBusStale(busTableBodyElement, false);
            renderDepartures(Array.from(merged.values()), busTableBodyElement, maxDeparturesLength);
        } catch (error) {
            console.error("Error parsing departures data:", error);
        }
    });
}


// Liniennamen, die zur Laufzeit umbenannt werden sollen (Server liefert die linke
// Variante, angezeigt wird die rechte). Bei Bedarf hier weitere Einträge ergänzen.
const lineReplacements = {
    REMEX12: "MEX12",
    REMEX18: "MEX18",
    RBRE6: "RE6",
    RBRE6b: "RE6b",
};

function lineLabel(line) {
    return lineReplacements[line] ?? line;
}

function timeFormat(timestamp) {
    const minutes = timestamp % 60;
    const hour = Math.floor(timestamp / 60);
    return hour > 0 ? `${hour} h ${minutes} Min` : `${minutes} Min`;
}



function initVdfiBus() {
    const body = document.getElementById("bus_table_body");
    if (!body) return;
    const { serverUrl, stopId, maxDepartures } = body.dataset;
    connectDepartureBoard(serverUrl, stopId, body, Number(maxDepartures));
}

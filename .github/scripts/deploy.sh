#!/bin/bash

# Author: Lukas Oertel <git@luoe.dev>
#
# Script to automate deployment

cd /srv/docker/fachschaftsempfaenger
/usr/bin/docker image pull python:3-alpine
/usr/bin/docker compose -f /srv/docker/fachschaftsempfaenger/docker-compose.yml build
/usr/bin/docker compose -f /srv/docker/fachschaftsempfaenger/docker-compose.yml up -d

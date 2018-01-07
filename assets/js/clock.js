function startTime() {
    var today=new Date();
    var wd=today.getDay();
    switch (wd) {
      case 1:
        wd="Montag";
        break;
      case 2:
        wd="Dienstag";
        break;
      case 3:
        wd="Mittwoch";
        break;
      case 4:
        wd="Donnerstag";
        break;
      case 5:
        wd="Freitag";
        break;
      case 6:
        wd="Samstag";
        break;
      case 0:
        wd="Sonntag";
        break;
      default:
        wd="Someday";
        break;
    }
    var d=today.getDate();
    var month=today.getMonth() + 1;
    var y=today.getFullYear();
    var h=today.getHours();
    var m=today.getMinutes();
    var s=today.getSeconds();

    var clock = h+":" +((m < 10) ? "0" : "")+m+":"+((s < 10) ? "0" : "")+s;
    var date = wd+", " +d+"."+month+"."+y;

    document.getElementById('time').innerHTML = clock;
    document.getElementById('date').innerHTML = date
    var t = setTimeout(function(){startTime()},500);
}

# Myanimewebsite


IMportant

var xmlhttp = new XMLHttpRequest();
var url = "https://gist.githubusercontent.com/phanirithvij/c7582f408b0d0fcd1eccba2803494068/raw/8b5ecd32ddf44f0b0a4a7d8db60bc09696ca954a/tot.json";
xmlhttp.open("GET", url, true);
xmlhttp.send();


then



v = xmlhttp.responseText


var ans = JSON.parse(v)



now



ans["002"].name




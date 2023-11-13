var place = {{station_content}}
var result = document.getElementById('result');
result.innerHTML = "";
for(var i=0; i < Object.keys(place).length; i++){
    result.innerHTML += "<p>" + place[i].staion_id + "</p>"
};


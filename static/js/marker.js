var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png"; 
var station = document.getElementById("station_list").innerText.split(',');
var imageSize = new kakao.maps.Size(24, 35); 
    
    // 마커 이미지를 생성합니다    
var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize); 
var positions = new Array();
for(var i=0; i<station.length; i++){
    var data = station[i];
    var data_content = station[i].split('|');
    
    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
        map: map, // 마커를 표시할 지도
        position: new kakao.maps.LatLng(data_content[2], data_content[3]), // 마커를 표시할 위치
        title : data_content[1], // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
        image : markerImage // 마커 이미지 
    });
    
}
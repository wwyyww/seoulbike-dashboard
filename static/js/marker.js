var imageSrc = "/static/assets/bicycle_marker.png"; 
var station = document.getElementById("station_list").innerText.split(',');
var imageSize = new kakao.maps.Size(40, 45);
    
    // 마커 이미지를 생성합니다    
var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize); 
var positions = new Array();

var clusterer = new kakao.maps.MarkerClusterer({
    map: map, // 마커들을 클러스터로 관리하고 표시할 지도 객체 
    averageCenter: true, // 클러스터에 포함된 마커들의 평균 위치를 클러스터 마커 위치로 설정 
    minLevel: 6 // 클러스터 할 최소 지도 레벨 
});
var markers = [];
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
    markers.push(marker);
}
clusterer.addMarkers(merkers);
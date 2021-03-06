$( document ).ready(function() {
    initTmap();

    $(".station").click(function() {
        var latitude = $(this).data("latitude");
        var longitude = $(this).data("longitude");
        removeTmap();
        initTmap();
        searchRoute(latitude, longitude);
    });

    $("#search_spots").click(function() {
        var minutes = $("#select option:selected").val();
        var longitude = $("#longitude").val();
        var latitude = $("#latitude").val();
        console.log(minutes);
        console.log(longitude);
        console.log(latitude);
        var data={
            startX: longitude,
            startY: latitude,
            preferred_time: minutes, 
        };
        $.ajax({
                type: "POST",
                url: "/possiblespot/",
                data: data,
                success: function(data) {
                    console.log(data);
                },
                error: function(error) {
                    console.log(error);
                }
            });
            return false;
    });

    $("#search_location").click(function() {
        var address = $("#sample4_roadAddress").val();
        var data={
            address_1: address
        };
        $.ajax({
                type: "POST",
                url: "/address/",
                data: data,
                success: function(data) {
                    console.log(data);
                    var latitude = data.latitude;
                    var longitude = data.longitude;
                    $('#latitude').val(latitude);
                    $('#longitude').val(longitude);

                    var lonlat = new Tmap.LonLat(longitude, latitude);
                    lonlat = lonlat.transform("EPSG:4326", "EPSG:3857");

                    var markers = new Tmap.Layer.Markers( "MarkerLayer" );
                    map.addLayer(markers);
                     
                    var size = new Tmap.Size(24,38);
                    var offset = new Tmap.Pixel(-(size.w/2), -size.h);
                    var icon = new Tmap.Icon('https://developers.skplanetx.com/upload/tmap/marker/pin_b_m_a.png', size, offset);  
                       
                    var marker = new Tmap.Marker(lonlat, icon);
                    markers.addMarker(marker);
                    map.setCenter(lonlat,15);
                },
                error: function(error) {
                    console.log(error);
                }
            });
            return false;

    });
});
function initTmap(){
    map = new Tmap.Map({div:'map_div',
                        width:'720px', 
                        height:'280px',
                        transitionEffect:"resize",
                        animation:true
                    }); 
    center = new Tmap.LonLat(127.0631412, 37.5150341);
    center.transform("EPSG:4326", "EPSG:3857");
    map.setCenter(center);
};

function removeTmap(){
    map.destroy();
};

//경로 정보 로드
function searchRoute(endX, endY){
    var routeFormat = new Tmap.Format.KML({extractStyles:true, extractAttributes:true});
    //var startX = 14129105.461214;
    //var startY = 4517042.1926406;
    //var endX = 14135591.321771959;
    //var endY = 4518111.822510956;
    var startX = 126.98217734415019;
    var startY = 37.56468648536046;
    //var endX = 129.07579349764512;
    //var endY = 37.17883196265564;
    var reqCoordType = "WGS84GEO";
    var urlStr = "https://apis.skplanetx.com/tmap/routes?version=1&format=xml";
    urlStr += "&reqCoordType="+reqCoordType;
    urlStr += "&startX="+startX;
    urlStr += "&startY="+startY;
    urlStr += "&endX="+endX;
    urlStr += "&endY="+endY;
    urlStr += "&appKey={{ api_key }}";
    var prtcl = new Tmap.Protocol.HTTP({
                                        url: urlStr,
                                        format:routeFormat
                                        });
    var routeLayer = new Tmap.Layer.Vector("route", {protocol:prtcl, strategies:[new Tmap.Strategy.Fixed()]});
    routeLayer.events.register("featuresadded", routeLayer, onDrawnFeatures);
    map.addLayer(routeLayer);
}
//경로 그리기 후 해당영역으로 줌
function onDrawnFeatures(e){
    map.zoomToExtent(this.getDataExtent());
}
    //본 예제에서는 도로명 주소 표기 방식에 대한 법령에 따라, 내려오는 데이터를 조합하여 올바른 주소를 구성하는 방법을 설명합니다.
function sample4_execDaumPostcode() {
    new daum.Postcode({
        oncomplete: function(data) {
            // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

            // 도로명 주소의 노출 규칙에 따라 주소를 조합한다.
            // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
            var fullRoadAddr = data.roadAddress; // 도로명 주소 변수
            var extraRoadAddr = ''; // 도로명 조합형 주소 변수

            // 법정동명이 있을 경우 추가한다. (법정리는 제외)
            // 법정동의 경우 마지막 문자가 "동/로/가"로 끝난다.
            if(data.bname !== '' && /[동|로|가]$/g.test(data.bname)){
                extraRoadAddr += data.bname;
            }
            // 건물명이 있고, 공동주택일 경우 추가한다.
            if(data.buildingName !== '' && data.apartment === 'Y'){
               extraRoadAddr += (extraRoadAddr !== '' ? ', ' + data.buildingName : data.buildingName);
            }
            // 도로명, 지번 조합형 주소가 있을 경우, 괄호까지 추가한 최종 문자열을 만든다.
            if(extraRoadAddr !== ''){
                extraRoadAddr = ' (' + extraRoadAddr + ')';
            }
            // 도로명, 지번 주소의 유무에 따라 해당 조합형 주소를 추가한다.
            if(fullRoadAddr !== ''){
                fullRoadAddr += extraRoadAddr;
            }

            // 우편번호와 주소 정보를 해당 필드에 넣는다.
            document.getElementById('sample4_postcode').value = data.zonecode; //5자리 새우편번호 사용
            document.getElementById('sample4_roadAddress').value = fullRoadAddr;
            document.getElementById('sample4_jibunAddress').value = data.jibunAddress;

            // 사용자가 '선택 안함'을 클릭한 경우, 예상 주소라는 표시를 해준다.
            if(data.autoRoadAddress) {
                //예상되는 도로명 주소에 조합형 주소를 추가한다.
                var expRoadAddr = data.autoRoadAddress + extraRoadAddr;
                document.getElementById('guide').innerHTML = '(예상 도로명 주소 : ' + expRoadAddr + ')';

            } else if(data.autoJibunAddress) {
                var expJibunAddr = data.autoJibunAddress;
                document.getElementById('guide').innerHTML = '(예상 지번 주소 : ' + expJibunAddr + ')';

            } else {
                document.getElementById('guide').innerHTML = '';
            }
        }
    }).open();
}

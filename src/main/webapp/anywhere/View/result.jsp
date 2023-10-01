<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="cpas.model.Food" %>
<%@ page import="java.util.List" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Food Locations</title>
    <script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=f5fb468455abb768835f1cae5f631b25&libraries=services"></script>
</head>
<body>

<div id="map" style="width:100%;height:1000px;"></div>

<script>
    var mapContainer = document.getElementById('map'), 
        mapOption = {
            center: new kakao.maps.LatLng(37.566826, 126.9786567), 
            level: 7 
        };

    var map = new kakao.maps.Map(mapContainer, mapOption); 
    var geocoder = new kakao.maps.services.Geocoder();

    function addressSearchCallback(address, storeName, storeTell) {
        return function(result, status) {
            if (status === kakao.maps.services.Status.OK) {
                var coords = new kakao.maps.LatLng(result[0].y, result[0].x);
                var marker = new kakao.maps.Marker({
                    map: map,
                    position: coords
                });

                var infowindow = new kakao.maps.InfoWindow({
                    content: '<div style="padding:10px; width:150px;">'
                            + '<b>가게 이름:</b> ' + storeName + '<br>'
                            + '<b>주소:</b> ' + address + '<br>'
                            + '<b>전화번호:</b> ' + storeTell + '<br>'
                            + '<button onclick="openRoute(' + result[0].y + ',' + result[0].x + ',\'' + address + '\')">길찾기</button>'
                            + '</div>'
                });


                kakao.maps.event.addListener(marker, 'click', function() {
                    // 클릭한 마커의 정보창이 이미 열려있다면 닫고, 아니면 열기
                    if (infowindow.getMap()) {
                        infowindow.close();
                    } else {
                        infowindow.open(map, marker);
                    }
                });
                
                map.setCenter(coords);
            }
        };
    }

    function openRoute(lat, lng, address) {
        var routeUrl = 'https://map.kakao.com/link/to/' + encodeURIComponent(address) + ',' + lat + ',' + lng;
        window.open(routeUrl, 'routePopup', 'width=600,height=600,scrollbars=yes,resizable=yes');
    }


    <%
        List<Food> foods = (List<Food>) request.getAttribute("foods");
        if (foods != null && !foods.isEmpty()) {
            for (Food food : foods) {
    %>
                var address = '<%= food.getStoreAddress() %>';
                var storeName = '<%= food.getStoreName() %>';
                var storeTell = '<%= food.getStoreTell() %>';
                geocoder.addressSearch(address, addressSearchCallback(address, storeName, storeTell));
    <%
            }
        }
    %>
</script>

</body>
</html>

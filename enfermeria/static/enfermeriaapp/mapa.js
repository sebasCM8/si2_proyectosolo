var map;
// alert("hello im js file");

var marker; 
function initMap() {
    var centro = { lat: -17.8060, lng: -63.1575 }; //Center location 
    map = new google.maps.Map(document.getElementById('map'), { zoom: 12, center: centro }); //map object 
    var lat = document.getElementById("lat").value;
    var lng = document.getElementById("lng").value;
    var punto = { lat: parseFloat(lat), lng: parseFloat(lng) };
    marker = new google.maps.Marker({ position: punto, map: map });
}
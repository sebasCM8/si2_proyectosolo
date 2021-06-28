var map;
// alert("hello im js file");

var marker; 
function initMap() {
    var centro = { lat: -17.8060, lng: -63.1575 }; //Center location 
    map = new google.maps.Map(document.getElementById('map'), { zoom: 12, center: centro }); //map object 
}
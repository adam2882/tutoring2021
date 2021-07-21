const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map', {
	preferCanvas: true
});
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);
const stations = JSON.parse(document.getElementById('stations-data').textContent);
var markers = L.markerClusterGroup();
markers.addLayer(L.geoJSON(stations, {
	pointToLayer: function (feature, latlng) {
		return L.circleMarker(latlng);
	}
}).bindPopup(function (layer) { return layer.feature.properties.name; }));
map.addLayer(markers);
map.setView([40, -121], zoom = 13);
//map.fitWorld();


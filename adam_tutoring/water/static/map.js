const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map')
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution, zoomOffset: 100 }).addTo(map);
/*const stations = JSON.parse(document.getElementById('stations-data').textContent);
let feature = L.geoJSON(stations).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map);*/
L.marker([50.5, 30.5]).addTo(map)


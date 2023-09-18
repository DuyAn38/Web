// Tạo một bản đồ Leaflet và đặt tọa độ và mức phóng to mặc định
var mymap = L.map('map').setView([40.701083, -74.1522848], 13);

// Sử dụng dịch vụ bản đồ miễn phí (ví dụ: OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(mymap);

// Thêm một đánh dấu (marker) tại tọa độ trung tâm
var marker = L.marker([40.701083, -74.1522848]).addTo(mymap);

// Thêm popup cho đánh dấu
marker.bindPopup("<b>Hello, World!</b><br>This is a sample marker.").openPopup();

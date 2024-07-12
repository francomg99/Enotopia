import reflex as rx

class GoogleMapComponent(rx.Component):
    def render(self):
        return rx.fragment(
            rx.div(id="map", style={"height": "400px", "width": "800px"}),
            rx.script(self.initialize_map())
        )

    def initialize_map(self):
        script_content = """
        function initMap() {
            var map = new google.maps.Map(document.getElementById('map'), {
                center: { lat: -33.000000, lng: -68.800000 },
                zoom: 8
            });

            var markersData = [
                { name: 'Luján de Cuyo', description: 'Famosa por sus Malbecs, esta región ofrece vinos de gran cuerpo y aromas frutales.', position: { lat: -33.000000, lng: -68.800000 } },
                { name: 'Valle de Uco', description: 'Con alturas elevadas, el Valle de Uco produce vinos con gran frescura y acidez.', position: { lat: -33.500000, lng: -69.200000 } }
            ];

            markersData.forEach(function(ig) {
                var marker = new google.maps.Marker({
                    position: ig.position,
                    map: map,
                    title: ig.name
                });

                var infoWindow = new google.maps.InfoWindow({
                    content: '<div><strong>' + ig.name + '</strong><br>' + ig.description + '</div>'
                });

                marker.addListener('click', function() {
                    infoWindow.open(map, marker);
                });
            });
        }

        // Cargar el script de Google Maps y luego inicializar el mapa
        function loadScript() {
            var script = document.createElement('script');
            script.src = "https://maps.googleapis.com/maps/api/js?key=TU_CLAVE_DE_API_DE_GOOGLE_MAPS&callback=initMap";
            script.async = true;
            script.defer = true;
            document.head.appendChild(script);
        }

        window.onload = loadScript;
        """
        return script_content

# Uso del componente en tu aplicación
google_map_component = GoogleMapComponent()

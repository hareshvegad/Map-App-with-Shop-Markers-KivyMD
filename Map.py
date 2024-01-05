from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.popup import Popup
from kivy.garden.mapview import MapMarker

KV = '''
BoxLayout:
    orientation: 'vertical'
    MapView:
        id: map_view
        lat: 18.52
        lon: 73.85
        zoom: 13
'''

class MapApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        # List of dictionaries with shop information
        shop_info = [
            {"lat": 18.52, "lon": 73.85, "shop_name": "BIBEWADI", "route_name": "Katraj"},
            {"lat": 18.58, "lon": 73.65, "shop_name": "BALAJI", "route_name": "Katraj"},
            {"lat": 18.58, "lon": 73.72, "shop_name": "VADGAON", "route_name": "Katraj"},
            {"lat": 18.65, "lon": 73.70, "shop_name": "DECCAN SANGVI", "route_name": "Katraj"},
            # Add more dictionaries as needed
        ]

        # Create markers based on coordinates
        for info in shop_info:
            lat, lon = info["lat"], info["lon"]
            marker = MapMarker(lat=lat, lon=lon, source="Map.png", on_press=lambda x, info=info: self.show_popup(info))
            self.root.ids.map_view.add_marker(marker)

    def show_popup(self, shop_info):
        # Create a popup with information and animation
        shop_name_label = MDLabel(
            text=f"Shop Name: {shop_info['shop_name']}",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1)
        )
        routlist_label = MDLabel(
            text=f"Rout Name: {shop_info['route_name']}",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1)
        )

        popup_content = BoxLayout(orientation="vertical")
        popup_content.add_widget(shop_name_label)
        popup_content.add_widget(routlist_label)

        popup = Popup(title="Shop Info", content=popup_content, size_hint=(None, None), size=(250, 175))
        popup.open()
        
    # def file_manager_open(self):
    #     self.file_manager_open(primary_ext_storage_path)
    #     self.manager_open = True
        
if __name__ == '__main__':
    MapApp().run()

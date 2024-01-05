Map App with Shop Markers

This simple Python application uses KivyMD and Kivy to create a map-based interface displaying shop markers. Each shop marker is associated with specific information, and clicking on a marker reveals a popup with details about the shop.
Prerequisites

Before running the application, ensure you have the following installed:

    KivyMD
    Kivy
    Kivy Garden MapView

You can install these dependencies using the following commands:

bash

pip install kivymd
pip install kivy
pip install kivy-garden
garden install mapview

Usage

    Clone the repository:

bash

git clone https://github.com/your_username/your_repository.git
cd your_repository

    Run the Map App:

bash

python map_app.py

    Explore the map with shop markers. Click on a marker to view shop information in a popup.

Code Overview

The main components of the code include:

    MapView: The main interface displaying the map with shop markers.

    Builder: Loads the Kivy language string for the interface.

    MapApp Class: Defines the application and its behavior.

        build: Loads the KV string to build the UI.

        on_start: Adds shop markers to the map during application start.

        show_popup: Displays a popup with detailed information about a selected shop.

Shop Information

Shop information is stored as dictionaries in the shop_info list. Each dictionary includes the latitude, longitude, shop name, and route name.

python

shop_info = [
    {"lat": 18.52, "lon": 73.85, "shop_name": "BIBEWADI", "route_name": "Katraj"},
    # Add more shop information dictionaries as needed
]

Feel free to expand the shop_info list with additional shop details.
Customization

    Marker Image: Replace the placeholder "Map.png" with your custom marker image.

    Popup Size: Adjust the size of the popup in the show_popup method.

    Popup Content: Customize the content of the popup by modifying the MDLabel widgets in the show_popup method.
'''
Folium-Script

'''


# Import module
# Note: Folium Module is not in the python standard library
import folium 

# Location vars
vienna = [48.210033, 16.363449]
europacamp = [48.1920, 16.3671]

# Instanciation of map object with start location and zoom level
m = folium.Map(location=vienna, zoom_start=12)

# Markers
folium.Marker(vienna).add_to(m)

folium.CircleMarker(
	location=vienna, 
	radius=59,
	color="#3186cc",
	fill=True,
	fill_color="#3186cc").add_to(m)


# saving map as html-file
m.save("vienna.html")

'''
Include code with ipinfo.io

import requests
r = requests.get('https://ipinfo.io')
data = r.json()
location = data['loc']


'''
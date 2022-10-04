import folium  
from operator import methodcaller

path = "gpsdata/gpsdata.txt"


with open(path, "r") as f:
	locations = f.read().split("\n")

m = folium.Map(location=[48.210033, 16.363449], zoom_start=12)

locations = list(map(methodcaller("split", ", "), locations))
print(locations)

m.save("loc2map.html")
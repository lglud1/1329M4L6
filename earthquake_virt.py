import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"

response = requests.get(url)
data = response.json()

earthquakes = data["features"]
magnitudes = [quake["properties"]["mag"] for quake in earthquakes]
times = [quake["properties"]["time"] for quake in earthquakes]

times = [datetime.fromtimestamp(time / 1000) for time in times]

plt.figure(figsize=(10, 6))
plt.plot(times, magnitudes, marker='o', linestyle='None', markersize=5, color='red')
plt.title('Recent Earthquake Activity')
plt.xlabel('Time')
plt.ylabel('Magnitude')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('earthquake_activity.png')

plt.show()

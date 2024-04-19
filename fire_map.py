import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.io import shapereader

file_path = "world_fires_1_day.csv"
data = pd.read_csv(file_path)

data = data.dropna(subset=['latitude', 'longitude'])

plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()
ax.coastlines()

sc = ax.scatter(data['longitude'], data['latitude'], c=data['brightness'],
                cmap='hot', s=10, transform=ccrs.PlateCarree(),
                alpha=0.7, edgecolors='none')

cbar = plt.colorbar(sc, orientation='vertical', shrink=0.5, label='Brightness')

plt.title('Global Fire Locations')
plt.tight_layout()
plt.show()

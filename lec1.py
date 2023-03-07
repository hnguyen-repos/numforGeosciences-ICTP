import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc
from mpl_toolkits.basemap import Basemap

file2 = "/home/ben/ictp/numforGeosciences-ICTP/datasets/lec1-era5_tas_1959_2021_25deg.nc"
f1 = nc.Dataset(file2)
lon = f1.variables['lon'][:]
lat = f1.variables['lat'][:]
var = f1.variables['t2m'][:,:,:]
varAverage = np.average(var, axis = 0)
lon, lat = np.meshgrid(lon, lat)

for i in range(756):
    m = Basemap(llcrnrlat=-80,urcrnrlat=80,llcrnrlon=0,urcrnrlon=360)
    m.drawcoastlines()
    m.pcolormesh(lon, lat, var[i,:,:],latlon=True, cmap='RdBu_r')
    plt.pause(0.05)
plt.show()
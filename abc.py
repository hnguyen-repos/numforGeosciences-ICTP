import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import netCDF4 as nc
from mpl_toolkits.basemap import Basemap
import time


file1= '/home/ben/ictp/numforGeosciences-ICTP/datasets/lec1-sample.txt'
data = np.loadtxt(file1)

# plt.subplot(1,2,1) # boxplot
# plt.boxplot(data) 
# plt.subplot(1,2,2) # histogram
# plt.hist(data, bins=10, rwidth=0.85, edgecolor = "k", density = 1.0)

# # kernel density estimation
# kde_obj = stats.gaussian_kde(data)
# x_pts = np.linspace(min(data)-1, max(data)+1, 100)
# estimated_pdf = kde_obj.evaluate(x_pts)
# # plt.plot(x_pts, estimated_pdf)

# plt.show()
df = pd.DataFrame(data)
print(df.describe())

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
    # time.sleep(0.1)
    plt.pause(0.05)
plt.title("Average Temperature")
plt.colorbar(location = "bottom")

plt.show()
import numpy as np
from datetime import datetime 
import matplotlib.pyplot as plt

class burl1_2011_data():
    
    def __init__(self, filename)
    
       fid = open(filename,'r')
dates = []; pres = []; speed = []; direction = []; uvel = []; vvel = [];

for line in fid.readlines()[2:]:
        dat = line.split()
        year = int(dat[0])
        month = int(dat[1])
        day = int(dat[2])
        hour = int(dat[3])
        minute = int(dat[4])
        dates.append(datetime(year,month,day,hour,minute))
        pres.append(float(dat[12]))
        speed.append(float(dat[6]))
        direction.append(float(dat[5])*(np.pi/180))

speed = np.array(speed)
direction = np.array(direction)
uvel = -speed*np.sin(direction)
vvel = -speed*np.cos(direction)
        
dates = np.array(dates)
pressure = np.array(pres)
otpt = np.array((dates,uvel,vvel,pressure))
print otpt
lat = 28.9; lon = 89.4
x, y = meshgrid(lat,lon)
q = plt.quiver(y[::6], x[::6], vvel[::6], uvel[::6], scale=100, color='b', linewidth=0.5)
plt.quiverkey(q,1,10,50,"5 m/s",coordinates='data',color='b')
plt.suptitle("Wind Vectors at Burl1 Met Station",size=15)
plt.grid=(True)
plt.title("North")
plt.xlabel("Latitudes [Degrees]")
plt.ylabel("Longitudes [Degrees]")
savefig('burl1_2011_wind_speed.pdf')

return otpt, self.year, self.uvel, self.vvel, self.pressure
# from serial import Serial
import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM17', 9600, timeout=1)
time.sleep(2)

DMAX = 4000
IMIN = 0
IMAX = 50

data = []

inc = []
for i in range(0,360):
    inc.append(i)

def update_line(num, data, line):
    scan = next(data)
    offsets = np.array([(np.radians(meas[1]), meas[2]) for meas in scan])
    line.set_offsets(offsets)
    intens = np.array([meas[0] for meas in scan])
    line.set_array(intens)
    return line

for i in range(360):
    line = ser.readline()   # read a byte string
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        stripped_string = string.strip()
        num = float(stripped_string) # convert the unicode string to an int
        print(num)
        data.append(num) # add int to data list
ser.close()

fig = plt.figure()
ax = plt.subplot(111, projection='polar')
line = ax.scatter([0, 0], [0, 0], s=5, c=[IMIN, IMAX],
                           cmap=plt.cm.Greys_r, lw=0)
ax.set_rmax(DMAX)
ax.grid(True)

ani = animation.FuncAnimation(fig, update_line,
    fargs=(data, line), interval=50)
plt.xlabel('Angle')
plt.ylabel('Distance')
plt.title('LIDAR 360 Sensor')
plt.legend()
plt.show()

# plt.plot(data,label = "Distance")
# plt.xlabel('Angle')
# plt.ylabel('Distance')
# plt.title('LIDAR 360 Sensor')
# plt.legend()
# plt.show()

# build the plot
# from serial import Serial
import serial
import time
import matplotlib.pyplot as plt

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM17', 9600, timeout=1)
time.sleep(2)

data = []

inc = []
# for i in range(0,360):
#     inc.append(i)

for i in range(360):
    line = ser.readline()   # read a byte string
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        stripped_string = string.strip()
        num = float(stripped_string) # convert the unicode string to an int
        print(num)
        data.append(num) # add int to data list
ser.close()

plt.plot(data,label = "Distance")
plt.xlabel('Angle')
plt.ylabel('Distance')
plt.title('LIDAR 360 Sensor')
plt.legend()
plt.show()

# build the plot
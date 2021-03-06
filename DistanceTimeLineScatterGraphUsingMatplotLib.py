import matplotlib.pyplot as plt

time = [0, 1, 2, 3]
position = [0, 100, 200, 300]

plt.plot(time, position,linestyle='dotted')
plt.xlabel('Time (hr)')
plt.ylabel('Position (km)')
plt.scatter(time, position)
plt.show()

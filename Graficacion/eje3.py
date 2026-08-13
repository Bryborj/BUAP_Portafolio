import matplotlib.pyplot as plt 
points = [(20,20), (80,20), (80,60), (20,60)]
x = [p[0] for p in points]
y = [p[1] for p in points]
plt.plot(x, y)
plt.xlim(0,100)
plt.ylim(0,100)
plt.grid()
plt.show()
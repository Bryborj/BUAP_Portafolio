import matplotlib.pyplot as plt 

pointsC = ([1,1], [2,1], [1,1],[1,3], [2,3])
pointsB = ([3, 1], [3,3], [4,3], [4,1], [3,1], [3,2], [4,2])
pointsL = ([5, 3], [5,1], [6, 1])
x = [p[0] for p in pointsC]
y = [p[1] for p in pointsC]
plt.plot(x, y)
x = [p[0] for p in pointsB]
y = [p[1] for p in pointsB]
plt.plot(x, y)
x = [p[0] for p in pointsL]
y = [p[1] for p in pointsL]
plt.plot(x, y)
plt.xlim(0,7)
plt.ylim(0,5)
plt.grid()
plt.show()
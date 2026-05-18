import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Vectors
u = np.array([2, 3, 1])
v = np.array([3, -2, -2])
u_plus_v = u + v

print(f"u: {u}")
print(f"v: {v}")
print(f"u + v: {u_plus_v}")

def area_triangle(p1, p2, p3):
    return 0.5 * np.linalg.norm(np.cross(p2 - p1, p3 - p1))

print(f"Area triangle heads (u, v, u+v): {area_triangle(u, v, u_plus_v)}")

origin = np.array([0, 0, 0])
area_O_u_u_plus_v = area_triangle(origin, u, u_plus_v)
area_O_v_u_plus_v = area_triangle(origin, v, u_plus_v)

print(f"Area triangle (O, u, u+v): {area_O_u_u_plus_v}")
print(f"Area triangle (O, v, u+v): {area_O_v_u_plus_v}")

# They should be equal to the area of O,u,v?
# Actually, u and u+v form a parallelogram with v. Area of triangle (O, u, u+v) is half of parallelogram, which is same as area(O, u, v).
print(f"Area triangle (O, u, v): {area_triangle(origin, u, v)}")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, u[0], u[1], u[2], color='r', label='u')
ax.quiver(0, 0, 0, v[0], v[1], v[2], color='b', label='v')
ax.quiver(0, 0, 0, u_plus_v[0], u_plus_v[1], u_plus_v[2], color='g', label='u+v')

ax.set_xlim([0, 5])
ax.set_ylim([-3, 4])
ax.set_zlim([-3, 2])
plt.legend()
plt.savefig('plot_vectors.png')

# Triangle rectangle
A = np.array([-1, 2, 1.5])
B = np.array([1, 2, 2])
C = np.array([1, 7, 1.5])

AB = np.linalg.norm(B - A)
BC = np.linalg.norm(C - B)
AC = np.linalg.norm(C - A)
print(f"AB: {AB}, BC: {BC}, AC: {AC}")
sides = sorted([AB, BC, AC])
print(f"Is right triangle? {np.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)}")


# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Caleb Mandapat
#               Mason McIntosh
#               Diego Arroyo
#               Lisandro Demagistris
# Section:      509
# Assignment:   12.13
# Date:         16 November 2023
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material
import numpy as np
import matplotlib.pyplot as plt

# Q1
x = np.linspace(-2.0, 2.0)

y = (1 / (4 * 2)) * x ** 2
z = (1 / (4 * 6)) * x ** 2

plt.plot(x, y, c='r', lw='2.0', label='f=2')
plt.plot(x, z, c='b', lw='6.0', label='f=6')
plt.title("Parabola plots with varying focal length")
plt.legend(loc="lower left")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

# Q2

x = np.linspace(-4, 4, 25)
y = (2 * x ** 3) + (3 * x ** 2) - (11 * x) - 6

plt.plot(x, y, c='y', marker='*', ls='', markeredgecolor='black')
plt.title('Plot of cubic polynomial')
plt.xlabel('x values')
plt.ylabel('y values')

plt.show()

# Q3

x = np.linspace(-2 * np.pi, 2 * np.pi)
y = np.cos(x)
z = np.sin(x)

plt.subplot(2, 1, 1)
plt.title('Plot of cos(x) and sin(x)')
plt.plot(x, y, c='r', label='cos(x)')
plt.ylabel('y=cos(x)')
plt.legend(loc='lower right')
plt.xticks([])
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(x, z, c='k', label='sin(x)')
plt.ylabel('y=sin(x)')
plt.legend(loc='upper right')
plt.grid()

plt.xlabel('x')

plt.show()

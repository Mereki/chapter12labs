# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Caleb Mandapat
# Section:      509
# Assignment:   12.14
# Date:         16 November 2023
#

import numpy as np
import matplotlib.pyplot as plt

mat = np.array([[1.02, 0.095], [-0.095, 1.02]])
pt = np.array([0, 1])

points = [pt]

for i in range(250):
    new_point = np.dot(mat, points[-1])  # multiply point by matrix
    points.append(new_point)  # add new point to list

arr = np.array(points)

plt.plot(arr[:, 0], arr[:, 1], linestyle='-', color='b')
plt.title('Spiral')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

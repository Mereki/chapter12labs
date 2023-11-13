# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Caleb Mandapat
#               Mason McIntosh
#               Diego Arroyo
#               Lisandro Demagistris
# Section:      509
# Assignment:   12.12
# Date:         13 November 2023
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import numpy as np
import matplotlib.pyplot as plt

a = np.matrix('0 1 2 3; 4 5 6 7; 8 9 10 11')
b = np.matrix('0 1; 2 3; 4 5; 6 7')
c = np.matrix('0 1 2; 3 4 5')

d = np.matmul(a, b)
d = np.matmul(d, c)

e = np.matrix(np.sqrt(d) / 2)
print(f'A = {a}')
print()
print(f'B = {b}')
print()
print(f'C = {c}')
print()
print(f'D = {d}')
print()
print(f'D^T = {np.transpose(d)}')
print()
print(f'E = {e}')

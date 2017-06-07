Solving quadratic equations of form ax^2 + bx + c to display the roots 
#Plotting quadratic functions of form y = ax^2 + bx + c

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

a1 = raw_input("Enter the first coefficient: ")
b1 = raw_input("Enter the second coefficient: ")
c1 = raw_input("Enter the third coefficient: ")

A = int(a1)
B = int(b1)
C = int(c1)

#the discriminant of the quadratic equation is given by
D = B**2 - (4*A*C)

if D >= 0:
    print ("The equation has two roots.")
    root1 = (-B + sqrt(D))/(2*A)
    root2 = (-B - sqrt(D))/(2*A)
    print "The first root is " + str(root1)
    print "The second root is " + str(root2)
else:
    print("The equation has no real roots.")

#plotting

h = (-1*B)/(2*A)
k = (A*(h**2)) + (B*h) + C

print(h)
print("The vertex is located at: ")
print("x = " + str(h))
print("y = " + str(k))

a =[]
b = []

for x in np.arange((int(h)-10),(int(h)+10),0.5):
    y = (A*(x**2)) + (B*x) + C
    a.append(x)
    b.append(y)

fig= plt.figure()
fig.suptitle('Graph of Quadratic Function')
axes = fig.add_subplot(111)
axes.set_xlabel('X')
axes.set_ylabel('Y')
#axes.set_ylim([-10,1000])
#axes.set_xlim([-10,10])
axes.grid(b=None, which='major', axis='both')
axes.plot(a,b)
axes.plot([h], [k], 'o')
plt.show()
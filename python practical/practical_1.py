# WAP to find the roots of a quadratic equation
import math
a = float(input("Enter coficient of x^2 : "))
b = float(input("Enter coficient of x : "))
c = float(input("Enter constant value : "))

d = b**2 - 4*a*c
print(d)
if d>0:
    x1 = (-b - math.sqrt(d))/2*a
    x2 = (-b + math.sqrt(d))/2*a
    print("Root of the equation are: ",x1, "and", x2)
else:
    print("roots are imaginary...!")
    
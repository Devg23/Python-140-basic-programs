#  Write a Python program to solve quadratic equation.
#  The standard form of a quadratic equation is:
#  ax2 + bx + c = 0
#  where
#  a, b and c are real numbers and
#  𝑎 ≠ 0
#  The solutions of this quadratic equation is given by:
 
#  (−𝑏 ± (b2 − 4𝑎𝑐 )/(2𝑎)

import math
a = int(input("Coefficeint of x^2 is : "))
b = int(input("Coefficeint of x is :"))
c = int(input("Value of Constant is : "))

discriminant = (b*b) - (4 * a * c)

if discriminant > 0:
    # when the roots are real and identical
    first = (- b + math.sqrt(discriminant) )/ (2*a)
    second =  (- b - math.sqrt(discriminant) )/ (2*a)

    print(f"Roots are {first} and {second}")
elif discriminant == 0:
    #Roots are real and distinct
    print(f"Roots are {-b/2*a} and {-b/2*a}")
else:
    #roots are complex
    real = -b / 2*a
    imaginary = math.sqrt(abs(discriminant))/2*a

    print(f"Roots are {real} + {imaginary}i and {real} - {imaginary}i")


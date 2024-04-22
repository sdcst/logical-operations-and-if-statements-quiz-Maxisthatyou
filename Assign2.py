"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math
x = float(input("Please enter a number> "))
y = float(input("Please enter another number> "))
z = input("Is one of the numbers the hypotenuse of a right triangle?> ")

if z == "yes":
    a = min( x, y )
    c = max( x, y )
    b = math.sqrt((c ** 2) - (a ** 2))
    b = round(b, 1)
    print(f"The missing side of this right triangle is {b}")
else:
    a = x
    b = y
    c = math.sqrt((a ** 2) + (b ** 2))
    c = round(c, 1)
    print(f"The hypotenuse of this right triangle is {c}")
Area calculations
square_side = float(input("What is the length of a side of the square? "))
square_area = float(square_side ** 2) 
print(f"The area of the square is: {square_area}")
print()
rectangle_length = float(input("What is the length of rectangle? "))
rectangle_width = float(input("What is the width of the rectangle? "))
rectangle_area = rectangle_length * rectangle_width
print(f"The area of the rectangle is: {rectangle_area}")
print()
circle_radius = float(input("What is the radius of the circle? "))
circle_area = 3.14 * (circle_radius ** 2)
print(f"The area of the circle is: {circle_area}")


#Calculations with 1 value
length = float(input("What is the common length of the shapes? "))
square_area = float(length ** 2) 
print(f"The area of the square is: {square_area}")
print()
import math
circle_area = math.pi * (length ** 2)
print(f"The area of the circle is: {circle_area}")
print()
cube_volume = length ** 3
print(f"The volume of a cube is {cube_volume}: ")
print()
sphere_volume = (4/3)*math.pi*(length ** 3)
print(f"The volume of the sphere is {sphere_volume}: ")



#Areas in cm^2 and m^2
square_side = float(input("What is the length of a side of the square? "))
square_area = float(square_side ** 2) 
print(f"The area of the square is: {square_area}  in cm^2")
print(f"The area of the square is: {square_area / 10000} in m^2")
print()
rectangle_length = float(input("What is the length of rectangle? "))
rectangle_width = float(input("What is the width of the rectangle? "))
rectangle_area = rectangle_length * rectangle_width
print(f"The area of the rectangle is: {rectangle_area} in cm^2")
print(f"The area of the rectangle is: {rectangle_area / 10000} in m^2")
print()
import math
circle_radius = float(input("What is the radius of the circle? "))
circle_area = math.pi * (circle_radius ** 2)
print(f"The area of the circle is: {circle_area} in cm^2")
print(f"The area of the circle is: {circle_area / 10000} in m^2")
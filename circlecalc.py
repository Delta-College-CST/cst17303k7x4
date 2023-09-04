# CST 173 - Delta College
# This program prompts for the radius of a circle.  It then
# calculates and displays the circumference and area.
import math

# Input rectangle attributes
print("For given circle:")
radius = float(input("==> Enter radius (inches): "))

# Processing
area = 2 * math.pi * radius
circumference = math.pi * radius**2

# Output
print()
print ("For circle with radius",radius,":")
print ("  Area: %6.2f square inches" % (area))
print ("  Circumference: %6.2f inches" %(circumference))


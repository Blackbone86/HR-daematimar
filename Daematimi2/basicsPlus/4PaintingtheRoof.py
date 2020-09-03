import math
length_cm = 50
degrees_str = input("Roof's angle in degrees: ")


# Convert input to integer
degrees_int = int(degrees_str)

# Convert degrees to radians in order to use the trigonometric functions in the math module
degrees_rad = math.radians(degrees_int)
# Calculate the the height of the triangle
height_cm = math.tan(degrees_rad) * 50


print("To make the platform level, the height must be", round(height_cm, 1), "cm")
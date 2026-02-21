import math

# 1. Ask the user for a number as input
number = float(input("Enter a number: "))

# 2. Use the math module to calculate the values
square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)

# Display the results
print(f"Square root: {square_root}")
print(f"Natural logarithm: {natural_log}")
print(f"Sine: {sine_value}")

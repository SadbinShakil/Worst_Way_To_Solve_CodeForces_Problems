import math

m = float(input("Enter M value: "))
n = float(input("Enter N value: "))
a = float(input("Enter a value: "))

first_row_flagstones = math.ceil(m/a)
iteration_count = math.ceil(n/a)

minimum_flagstone_needed = first_row_flagstones * iteration_count
print(f"minimum flagstone needed= {minimum_flagstone_needed}")
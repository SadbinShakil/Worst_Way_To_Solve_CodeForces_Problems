import math


print("enter Board Sizes is Square M, N: ")
M = int(input("Enter value for M: "))
N = int(input("Enter value for N: "))

print(f"The maximal number of dominoes= {math.floor((M*N)/2)}")
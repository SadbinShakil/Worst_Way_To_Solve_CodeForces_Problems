input_int = int(input("Enter the input int: "))
nth       = int(input("Enter how many times will be subtract: "))

last_digit = int(repr(input_int)[-1])
temp = 0

def subtract(n):
    n = n - 1
    return n

def divide(n):
    n = n//10
    return n


for i in range(nth):
    if(last_digit == 0):
        input_int = divide(input_int)
        last_digit = int(repr(input_int)[-1])
    else:
        input_int = subtract(input_int)
        last_digit = int(repr(input_int)[-1])

print(input_int)

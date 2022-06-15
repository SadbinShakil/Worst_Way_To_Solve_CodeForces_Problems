input_string = input("enter your input string: ")
count = 0

if(input_string.isnumeric() == True):
    for digit in input_string:
        if(int(digit) == 4 or int(digit) == 7):
            count = count +1
        else:
            pass

    if(count == 4 or count == 7):
        print("Yes! Nearly Lucky")
    else:
        print("No! Not Nearly Lucky")
else:
    print("Invalid Input")
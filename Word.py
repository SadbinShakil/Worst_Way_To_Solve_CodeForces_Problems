input_string = input("enter your input string: ")

count_up   = 0
count_down = 0


if(input_string.isalpha()==True):

    for char in input_string:
        if(char.isupper()==True):
            count_up = count_up + 1
        elif(char.isupper() == False):
            count_down = count_down + 1
        else:
            pass

    if(count_up>count_down):
        print(input_string.upper())
    elif(count_up<count_down):
        print(input_string.lower())
    else:
        print(input_string.lower())
else:
    print("Invalid Input String")
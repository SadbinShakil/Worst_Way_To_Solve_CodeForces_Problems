X = 0
Check = ['X','+','-']
check2 = ['X--','--X']
check3 = ['X++','++X']
count = 0
count_for_each_string = []


Test_Case = int(input("enter how many test cases you need: "))
Input_String = []
for string in range(0,Test_Case):
    temp = input("Enter the input string: ")
    Input_String.append(temp)

for string in Input_String:
    for character in string:
        if character in Check:
            #print("OK!")
            count += 1
        else:
            print("Input type NOT OK!")
    #print(count)
    count_for_each_string.append(count)
    count = 0
print(count_for_each_string)

if all(x==count_for_each_string[0] for x in count_for_each_string):
    for string in Input_String:
        if string in check2:
            X = X - 1
        elif string in check3:
            X = X + 1
        else:
            print("Wrong Input type...")
else:
    print("Hehe")
    


print(X)


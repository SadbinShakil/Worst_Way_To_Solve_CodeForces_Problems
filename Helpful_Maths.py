string = input("Enter the input string: ")
output_string = []
checklist = ['+']
temp = []
print("Your Input was: ", string)

for i in string:
    if(i != '+'):
        temp2 = int(i)
        temp.append(temp2)
        
temp.sort()

print(temp)
print('+'.join(str(x) for x in temp))
    # print(string[i])

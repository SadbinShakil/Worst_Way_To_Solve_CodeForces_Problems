input_string = input("enter your input string: ")
input_string = sorted(input_string)
count = 0

for i in range(len(input_string) - 1):
    if(input_string[i]!= input_string[i+1]):
        count = count + 1
    else:
        pass

if(count % 2 == 0):
    print(" IGNORE HIM! ")

else:
    print("CHAT WITH HER! ")
string1 = input("Enter your first String: ")
string2 = input("Enter your second String: ")

count = 0
for i in range(len(string1)):
    if(string1[i].lower()==string2[i].lower()):
        count = count + 1

if count == len(string1):
    print("0")
else:
    for i in range(len(string1)):
        if(string1[i].lower()>string2[i].lower()):
            print("1")
            break

        elif(string1[i].lower()<string2[i].lower()):
            print("-1") 
            break


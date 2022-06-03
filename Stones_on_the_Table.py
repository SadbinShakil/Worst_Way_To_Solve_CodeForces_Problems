temp = int(input("enter the length of the string: "))
input_string = input("enter your input string: ")
count = 0
output = []

for i in range(len(input_string) - 1):
    if(input_string[i] == input_string[i+1]):
        count = count + 1
    else:
        output.append(count)
        count = 0
output.append(count)
    
output = [i for i in output if i != 0]  
print(temp) 
print(min(output))
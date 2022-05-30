string = input("Enter your input String: ")
vowel_Check = ['a','e','i','o','u']
output_string = []
for i in range(len(string)):
        if string[i].lower() in vowel_Check:
            output_string.append(".")
        else:
            output_string.append(string[i])
            # print("PAisi")

print(output_string)            
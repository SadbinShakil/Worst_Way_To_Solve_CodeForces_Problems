word = input("enter the input word: ")
word_list = []
if (word != ""):
    for character in word:
        word_list.append(character)
else:
    print("Input word can't be empty...")

for item in word_list:
    if(item == word_list[0]):
        word_list[0]=item.upper()
    else:
        pass

    
final_output = ' '.join([str(item) for item in word_list])
print(final_output)


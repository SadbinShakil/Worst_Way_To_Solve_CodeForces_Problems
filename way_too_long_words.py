n = int(input("enter word count: "))
list_of_words = []
for word in range(0,n):
    list_of_words.append(input(f"enter {word} word: "))

print(list_of_words)


def converting_list_to_string(lis):
    listToStr = ''.join([str(elem) for elem in lis])
    print(listToStr)


def make_abbreviation(word):
    abbreviation_list = []
    counter = 0
    length = len(word)
    for position in range(0,length):
        if position==0 or position==length-1:
            abbreviation_list.append(word[position])
        else:
            counter += 1
            if counter==length-2:
                abbreviation_list.append(counter)
                
    converting_list_to_string(abbreviation_list)
    
        
                     
for word in list_of_words:
    if len(word)<=10:
        print(word)
    else:
        make_abbreviation(word)







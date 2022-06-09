input_string = input("Enter the players sequesnce: ")
check = 0
final_check = 0
player_count = []
if(input_string != ""):
    if(all(c in '01' for c in input_string)):
        for i in range(len(input_string)-1):
            if(input_string[i] == input_string[i+1]):
                check = check + 1
            else:
                if(check>0):
                    check = check + 1
                    player_count.append(check)
                    check = 0
                else:
                    pass
        if(check>0):
            check = check + 1
            player_count.append(check)
        # print(player_count)

        for i in player_count:
            if(i>=7):
                final_check = final_check + 1
            else:
                pass
        if(final_check==0):
            print("Not Dangerious")
        else:
            print("Dangerious")
    
    else:
        print("Input string can't contain any character other than 0 and 1...")
else:
    print("Input string Can't be Empty..")

CFhouse = int(input("Enter the co-ordinate of friend's house: "))
#approach 1
# if(CFhouse % 5 == 0):
#     print("Steps required: ", (CFhouse//5))
# else:
#     print("Steps required: ", (CFhouse//5)+1)






#approach 2

temp = 0
steps_needed = 0


def checking(rcf, temp, steps_needed):
    if(rcf>=4 and rcf<5):
        temp = rcf//4
        steps_needed = steps_needed + temp

        if(CFhouse%4 == 0):
            print("Steps required: ",steps_needed)
        else:
            checking(CFhouse%4, temp, steps_needed)

    if(rcf>=3 and rcf<4):
        temp = rcf//3
        steps_needed = steps_needed + temp

        if(CFhouse%3 == 0):
            print("Steps required: ",steps_needed)
        else:
            checking(CFhouse%3, temp, steps_needed)

    if(rcf>=2 and rcf<3):
        temp = rcf//2
        steps_needed = steps_needed + temp

        if(CFhouse%2 == 0):
            print("Steps required: ",steps_needed)
        else:
            checking(CFhouse%2, temp, steps_needed)

    if(rcf>=1 and rcf<2):
        temp = rcf//1
        steps_needed = steps_needed + temp

        if(CFhouse%1 == 0):
            print("Steps required: ",steps_needed)
        else:
            checking(CFhouse%1, temp, steps_needed)





if(CFhouse != ""):
    if(CFhouse==0):
        print("Steps required: 0")
    else:
        if(CFhouse>=5):
            temp = CFhouse//5
            steps_needed = steps_needed + temp
            if(CFhouse%5 == 0):
                print("Steps required: ",steps_needed)
            else:
                checking(CFhouse%5, temp, steps_needed)
        else:
            checking(CFhouse%5, temp, steps_needed)

else:
    print("Can't be an empty input..")

            

    
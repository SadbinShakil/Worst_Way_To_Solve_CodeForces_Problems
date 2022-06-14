n = int(input("Enter how many train stoppage are there: "))
entering = []
leaving  = []
final    = []
total_leave = 0
total_enter = 0
temp3       = 0


for i in range(n): 
    leave = int(input())
    enter = int(input())
    leaving.append(leave)
    entering.append(enter)

    temp3 = temp3 - leave
    temp3 = temp3 + enter
    final.append(temp3)
    
print("The minimum possible capacity of the tram: ", max(final))




    

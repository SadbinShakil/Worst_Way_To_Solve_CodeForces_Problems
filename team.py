num_of_problems = int(input("Enter the number of problems here: "))
num_of_peoples = int(input("Enter the number of peoples here: "))

list_of_known_unknown = [[]]


for i in range(0,num_of_problems):
    ans =[]
    for j in range(0,num_of_peoples):
        b = int(input("enter 0/1: "))
        if b == 0 or b==1:
            ans.append(b)
        else:
            print("wrong input. Only 0/1")
            exit()
    list_of_known_unknown.append(ans)

#print(list_of_known_unknown)

list_of_known_unknown= [x for x in list_of_known_unknown if x] #eliminating empty list
print(f"Final answers List is {list_of_known_unknown}")

length = len(list_of_known_unknown)
print(f"length of the answers list is {length}")
out = 0

for list in list_of_known_unknown:
    c = 0
    leng = len(list)
    #print(f"length of first list {leng}")
    for i in range(0,leng):
        if(list[i]==1):
            c += 1
            #print(f"c {c}")
    if c>=2:
        out += 1
        #print(f"out {out}")


print(f"The number of problems they will implement is {out}")

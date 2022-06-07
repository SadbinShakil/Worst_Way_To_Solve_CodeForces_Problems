row = int(input("Enter how many rows you want: "))
sum1 = 0
sum2 = 0
sum3 = 0
InputMatrix = []


for i in range(0,row):
    a = []
    for j in range(0,3):
        val = int(input())
        a.append(val)
    InputMatrix.append(a)
   
print("This is the Matrix you have inserted: ")
for i in range(0,row):
    for j in range(0,3):
        print(InputMatrix[i][j], end="  ")
    print( )

for i in range(0,row):
    for j in range(0,3):
        pass
    sum1 = sum1 + InputMatrix[i][0]
    sum2 = sum2 + InputMatrix[i][1]
    sum3 = sum3 + InputMatrix[i][2]
      
print("Total sum for each vectors: ",sum1,sum2,sum3)
if(sum1 == 0 and sum2 == 0 and sum3 == 0):
    print("YES")
else:
    print("NO")

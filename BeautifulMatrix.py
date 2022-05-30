columns = int(input("Enter how many Columns you needed:  "))
rows    = int(input("Enter how many Rows you needed: "))

print("Enter your input Matrix: ")

# InputMatrix = [[1,2,3],[1,2,3],[1,2,3],[1,2,3]]
InputMatrix = []
for i in range(rows):
    a = []
    for j in range(columns):
        val = int(input())
        a.append(val)
    InputMatrix.append(a)
   

#For printing the matrix
print("This is the Matrix you have inserted: ")
for i in range(rows):
    for j in range(columns):
        print(InputMatrix[i][j], end="  ")
    print( )
 

for i in range(rows):
    for j in range(columns):
       if(InputMatrix[i][j]==1):
           output = abs(i-3)+abs(j-3)
    


print("Desire steps are: ",output)  



   
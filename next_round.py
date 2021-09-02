n = int(input("enter total input count: "))
position = int(input("Enter the given position: "))

inputs = []
count = 0
print(f"give {n} inputs: ")
for i in range(0,n):
    a = int(input())
    inputs.append(a)

for value in inputs:
    print(f"checking {inputs[position]} and {value}")
    if value >= inputs[position]:
        count += 1

print(f"Expected output is: {count}")

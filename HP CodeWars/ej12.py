import math

n = int(input())
output = []

for i in range(n):
    x = input().split()
    if x[0] == "rectangle":
        y = float(x[1])*float(x[2])
    
    elif x[0] == "circle":
        y = math.pi*float(x[1])**2
    
    output.append(y)

for j in range(n):
    result = output[j]
    result = f"{result:.6f}"
    print(result)
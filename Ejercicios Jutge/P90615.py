inputs = input().split()
while len(inputs) < 3:
    inputs2 = input().split()
    if inputs2:
        inputs.append(inputs2[0])
val1 = int(inputs[0])
val2 = int(inputs[1])
val3 = int(inputs[2])
if val1 == val2 or val1 == val3:
    print(val1)
elif val2 == val1 or val2 == val3:
    print(val2)
elif val1 > val2 and val1 > val3:
    print(val1)
elif val2 > val1 and val2 > val3:
    print(val2)
else:
    print(val3)
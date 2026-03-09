num=input().split()
intNum = []
num.sort()
errors = 0

for j in num:
    intNum.append(int(j))

for i in range(max(intNum)-min(intNum)):
    if not i+min(intNum) in intNum:
        errors += i+min(intNum)
print(errors)
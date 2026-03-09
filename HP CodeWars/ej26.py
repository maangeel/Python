import sys

min = 1
max,maxOpAllow = map(int(input()))
numSubAdd = max//2

for i in range(numSubAdd):
    print(f"SUB {numSubAdd}")
    print("CHECK")
    sys.stdout.flush()
    correct = input()
    if correct == "NEGATIVE":
        max -= numSubAdd
        answer = max+min//2
    elif correct == "POSITIVE":
        min = num+1
        num = (min+num-1)//2
    elif correct == "Correct":
        break
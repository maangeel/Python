import sys
num = 50
min = 0
max = 100

for i in range(50):
    print(num)
    sys.stdout.flush()
    correct = input()
    if correct == "Higher":
        min = num+1
        num = (max+num+1)//2
    elif correct == "Lower":
        max = num-1
        num = (min+num-1)//2
    elif correct == "Correct":
        break
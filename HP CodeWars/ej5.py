num = int(input())

if num >= 1 and num <= 9:
    if num == 1:
        print("one")
    if num == 2:
        print("two")
    if num == 3:
        print("three")
    if num == 4:
        print("four")
    if num == 5:
        print("five")
    if num == 6:
        print("six")
    if num == 7:
        print("seven")
    if num == 8:
        print("eight")
    if num == 9:
        print("nine")

elif num%2==0:
    print("even")
else:
    print("odd")
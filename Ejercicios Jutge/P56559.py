a1, b1, a2, b2 = map(int, input().split())

if a1 == a2 and b1 == b2:
    print("=")
elif a1 <= a2 and b1 >= b2:
    print("2")
elif a1 >= a2 and b1 <= b2:
    print("1")
else:
    print("?")
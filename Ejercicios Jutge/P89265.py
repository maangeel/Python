a1, b1, a2, b2 = map(int, input().split())

if a1 == a2 and b1 == b2:
    printRule = "="
elif a1 <= a2 and b1 >= b2:
    printRule = "2"
elif a1 >= a2 and b1 <= b2:
    printRule = "1"
else:
    printRule = "?"

x = max(a1, a2)
y = min(b1, b2)

if x <= y:
    print(f"{printRule} , [{x},{y}]")
else:
    print(f"{printRule} , []")
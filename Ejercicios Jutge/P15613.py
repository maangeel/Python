temp = int(input())
if temp <= 0:
    print("it's cold")
    print("water would freeze")
elif temp >= 100:
    print("it's hot")
    print("water would boil")
elif temp >= 10 and temp <= 30:
    print("it's ok")
elif temp > 0 and temp < 10:
    print("it's cold")
elif temp > 30 and temp <= 100:
    print("it's hot")
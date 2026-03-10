nights = int(input())
price = int(input())

total= 0
priceFixed = price

for i in range(nights):
    total+=priceFixed
    priceFixed= 0.9*price

print(int(total))
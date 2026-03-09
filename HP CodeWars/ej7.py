x = int(input())
xlist = []

for i in range(x):
    y = int(input())
    xlist.append(y)

resta = max(xlist)-min(xlist)
if resta not in xlist:
    print(':(')
else:
    print(":)")
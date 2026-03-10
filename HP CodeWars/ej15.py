i = input()
reverseI = i[::-1]
orig=[ch for ch in i]
if i == reverseI:
    print(0)
else:
    isplit=[ch for ch in i]
    isplitrev=isplit[::-1]
    isplitrev.pop(0)
    while isplit!=isplitrev:
        for x in isplitrev:
            isplit.append(x)
    print(len(isplit)-len(orig))

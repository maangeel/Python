names = input().split()
ordered = sorted(names)
if names[0] == names[1]:
    print(names[0],"=",names[1])
else:
    if names[0] == ordered[0]:
        print(names[0],"<",names[1])
    else:
        print(names[0],">",names[1])
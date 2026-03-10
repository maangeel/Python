Ax, Ay=input().split()
Bx, By=input().split()
Dx, Dy=input().split()
if int(Ax)<int(Bx) and int(Ax)<int(Dx) and int(Ax)<=100:
    print("GOAL")
else:
    print("OFFSIDE")

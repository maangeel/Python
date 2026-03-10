n=int(input())
camino=input().split("X")

result = []

for i in camino:
    
    ii=[a for a in i]
    if len(ii)>=n:
        for j in range(n):
            ii[j]="*"
        
print("X".join(camino))

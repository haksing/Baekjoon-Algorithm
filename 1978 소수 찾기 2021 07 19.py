N = int(input())
a = list(map(int,input().split()))
z = 1
point = N
for i in range(0,N):
    if a[i]==1:
        point = point -1
        continue
    
    for z in range (2,a[i]):
        if a[i]%z==0:
            point = point -1
            break

print(point)
N=int(input())
a = list(map(int,input().split()))
k = 2
t = 0
m = max(a)*2
while True:
    point = 0
    for i in range(0,N):
        if m%a[i]==0:
            point +=1
        if point == N:
            t = 1
    
    if t==1:
        t = 0
        
        for z in range(2,m):
            if m %z==0:
                t +=1
        if t!=N:
            k = k + 1    
            m = max(a) * k
            continue
        elif t==N:
            print(m)
            break


    k = k + 1    
    m = max(a) *k
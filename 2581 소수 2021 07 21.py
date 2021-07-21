N = int(input())
M = int(input())
a = []
sum = 0



for i in range(N,M+1): # N부터 M사이의숫자를 넣는 반복문
    if i == 2:
        a.append(i)
        continue
    if i==1:
        continue
    for z in range(2,i):
        t = 0
        if i%z==0:
            t = 1
            break
    if t == 0:
        a.append(i)



if len(a)==0:
    print('-1')
else:
    for i in a: 
        sum = sum + int(i)
    min_a = min(a)

    print(sum)
    print(min_a)


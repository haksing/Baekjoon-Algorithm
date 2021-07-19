T = int(input())
a = []
for i in range (0,T):
    l = list(map(int, input().split()))
    a.append(l)

def point(list):
    x1 = list[0]
    y1 = list[1]
    r1 = list[2]
    x2 = list[3]
    y2 = list[4]
    r2 = list[5]
    r3 = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    if r2>r1:
        temp = r1
        r1 = r2
        r2 = temp
    if r3==0:
        if r1==r2: #중심이 같을 떄
            return -1
        elif r1!=r2:
            return 0

    elif r3==r1+r2: # 접할 때
        return 1
    elif r3>r1+r2: 
        return 0
    elif r3<r1+r2:
        if r3+r2 < r1:
            return 0
        elif r3+r2 == r1:
            return 1
        else:
            return 2

for i in range(0,T):
    print('%d' %point(a[i]))


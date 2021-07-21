A,B,V = map(int,input().split())
day = 0
afternoon = 0
while True :
    afternoon =  afternoon + A
    day +=1
    if afternoon >= V:
        break
    else:
        afternoon = afternoon - B

print(day)
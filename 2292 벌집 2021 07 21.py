N = int(input())
a=2
b=1
i=0
while True:
    
    if N==1:
        print('1')
        break
    else:
        a = a+(6*i)
        b = b+(6*(i+1))
        if a<=N and b>=N:
            min_room = i+2
            print(min_room)
            break
        else:
            i +=1



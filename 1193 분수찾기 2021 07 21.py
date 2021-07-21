number = int(input())
i = 1
while True :
    
    number = number - i
    if number <= 0 :
        counting = number + i
        c = i
        break
    elif number >0:
        i += 1
m = 0 # 분모 i는 분자이다.
i = i+1


for z in range(counting):
        i = i-1
        m = m+1

if c%2==0:
    print('%d/%d' %(m,i))
else:
    print('%d/%d' %(i,m))
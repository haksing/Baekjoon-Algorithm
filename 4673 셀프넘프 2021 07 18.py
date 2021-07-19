s1 = [] #1부터 10000까지 리스트
s2 = []
sum = 0
for i in range(1,10001):
    s1.append(i)

for i in range (1,10001):
    inza = i
    while True:
        m = inza//10
        n = inza%10
        if m==0:
            sum = sum + n + i
            s2.append(sum)
            sum = 0
            break
        sum = sum + n
        inza = m

s2.sort()
s3= set(s1)-set(s2)
s4=list(s3)
s4.sort()

   
for i in range(0,len(s4)):
    print(s4[i])
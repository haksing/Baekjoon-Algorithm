from collections import deque
import sys
q = deque()
z= 0


N = int(input())
a = []
for i in range(N):
    b = int(sys.stdin.readline())
    a.append(b)

i = 1
s = [] # 수열이 맞는지 확인용
count = [] #+ , - print용
for i in (1,N+1):
    q.append(i)
    if a[z]==q[-1]:
        s.append(q.pop())
        z+=1
        count.append('-')
    else:
        i = i + 1
        count.append('+')
    
for i in range(len(q)):
    s.append(q.pop())
    count.append('-')

if a==s:
    for i in range(0,len(count)):
        print(count[i])
else:
    print('NO')

        


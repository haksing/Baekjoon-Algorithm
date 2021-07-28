from collections import deque
import sys 
q = deque()
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
s= [] #오큰수 저장소

for i in range(0,N):

    if i==N-1:
        s.append(-1)
    else:
        for z in range(i+1,N):
 
            if a[i]<a[z]:
                s.append(a[z])
                break
            elif z==N-1:
                s.append(-1)
                break


for i in range(len(s)):
    print(s[i], end = ' ')




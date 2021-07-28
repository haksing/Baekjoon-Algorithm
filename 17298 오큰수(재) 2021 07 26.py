import sys
from typing import Deque 
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
q = Deque()

result = [-1 for _ in range (N)]

q.append(0)
i = 1

while q and i<N:

    while q and a[q[-1]] < a[i]:
        result[(q.pop())] = a[i]

    q.append(i)
    i+=1 


for i in range(0,N):
    print(result[i] , end = ' ')
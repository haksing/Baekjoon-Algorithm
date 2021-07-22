import sys
from collections import deque
N = int(sys.stdin.readline())

q = deque()

for i in range(N):
    ary = sys.stdin.readline().strip()
    q = deque()
    yes_or_no = 1
    for i in ary:
        if i=='(':
            q.append(i)
        elif i==')':
            if len(q)==0:
                yes_or_no = 0
                break
            else:
                q.pop()
    
    if yes_or_no==0 or len(q)!=0:
        print('NO')
    elif yes_or_no==1 and len(q)==0:
        print('YES')
    
    




import sys
from collections import deque
queue = deque([])
N = int(sys.stdin.readline())
count = 0
for i in range(N):
    input = sys.stdin.readline().split()

    if input[0]=='push':
        queue.append(int(input[1]))
        count +=1
    elif input[0]=='pop':
        if count==0:
            print(-1)
        else:
            print(queue.popleft())
            count -=1
    elif input[0]=='size':
        print(count)
    elif input[0]=='empty':
        if count==0:
            print(1)
        else :
            print(0)
    elif input[0]=='front':
        if count==0:
            print(-1)
        else :
            print(queue[0])
    elif input[0]=='back':
        if count==0:
            print(-1)
        else:
            print(queue[-1])




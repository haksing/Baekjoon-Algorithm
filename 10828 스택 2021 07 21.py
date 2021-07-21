
import sys
N = int(input())
stack = []
top = -1
for i in range(N):
    a= (sys.stdin.readline())
    if a[:4] =='push':
        top = top+1
        stack.insert(top,int(a[5:]))
    elif a[:3]=='pop':
        if top==-1:
            print(-1)
        else:
            print(stack[top])
            stack.pop()
            top = top -1
    elif a[:3]=='top':
        if top ==-1:
            print('-1')
        else:
            print(stack[top])
    elif a[:4] == 'size':
        print(len(stack))
    elif a[:5]=='empty':
        if top==-1:
            print(1)
        else:
            print(0)
        
        


from collections import deque
import sys


while True :
    a = sys.stdin.readline()
   
    if a[0]=='.':
        break # 마지막 문장이 '.'이면 반복 종료
    stack = deque() #덱 선언 파이썬에서는 스택 큐 모두 덱이용하는 것이 좋음
    errorcord = 0

    
    for i in a:

        if i=='(':
            stack.append(i)
        elif i=='[':
            stack.append(i)
        elif i==')':
            if len(stack)==0 or stack[-1]=='[':
                errorcord = 1
                break
            else:
                stack.pop()
        elif i==']':
            if len(stack)==0 or stack[-1]=='(':
                errorcord = 1
                break
            else:
                stack.pop()

    if errorcord==1 or len(stack) != 0:
        print('NO')
    else:
        print('YES')         

            


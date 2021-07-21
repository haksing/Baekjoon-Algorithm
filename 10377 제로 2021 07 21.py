import sys
stack = []
K = int(input())
for i in range(K):
    input = int(sys.stdin.readline())
    if input==0:
        stack.pop()
    else:
        stack.append(input)

lens = len(stack)
sum = 0
for i in range(lens):
    sum = sum + stack[i]

print(sum)


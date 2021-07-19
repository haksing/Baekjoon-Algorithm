N = int(input())
t=1
for i in range(1,N+1):
    print('%s' %' '*(N-t),end='')
    t +=1
    for z in range(1,i+1):
        print('*', end='')
    print('')

    
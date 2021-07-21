number = int(input())
i = 1
while True :
    
    number = number - i
    if number <= 0 :
        counting = number + i
        c = i
        break
    elif number >0:
        i += 1
m = 0 # 분모 i는 분자이다.
i = i+1


for z in range(counting):
        i = i-1
        m = m+1

if c%2==0:
    print('%d/%d' %(m,i))
else:
    print('%d/%d' %(i,m))

# 대각으로 1씩 증가하는 등차수열임으로 받은수에서 
# 1씩 증가시키면서 빼면 0보다 0보다 작거나같은경우 멈춘다 . 마지막에 몇을
# 빼주었는지 확인 후 그 수가 대각선의 라인이 된다. 
# 그리고 홀수와 짝수 대각선의 print하는 방식이 다르다는 걸 입력방식만
# 다르게 하여서 풀었다.
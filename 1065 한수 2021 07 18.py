N = (input())
score = 0
for i in range(1,int(N)+1):
    if len(str(i))==1 or len(str(i))==2:
        score += 1
    elif len(str(i))==3:
        num = str(i)
        if int(num[0])-int(num[1]) == int(num[1])-int(num[2]):
            score += 1
        else:
            continue
    else:
        continue

print(score)




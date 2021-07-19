string = input()
i = 0
point = 0
len = len(string)
while True:
    if i==len-1:
        point +=1
        break
    if string[i]=="c"and string[i+1] =="=":
        point +=1
        i += 2
    elif string[i]=="c" and string[i+1] =="-":
        point +=1
        i += 2
    elif string[i]=="d"and string[i+1]=='z':
        if i==len-2:
            point +=2
            break
        elif i<len-2 and string[i+2]=='=':
            point +=1
            i +=3
        else:
            point +=2
            i +=2
    elif string[i]=="d"and string[i+1]=='-':
        point +=1
        i+=2
    elif string[i]=="l"and string[i+1]=='j':
        point +=1
        i+=2
    elif string[i]=="n"and string[i+1]=='j':
        point +=1
        i+=2
    elif string[i]=="s"and string[i+1]=='=':
        point +=1
        i+=2
    elif string[i]=="z"and string[i+1]=='=':
        point +=1
        i+=2
    else:
        point +=1
        i+=1
    if i==len:
        break

print(point)
 # 1 런타임 에러 이유 마지막 문자가 앞자리 c같은 문자라면 다음번째 인덱스를
 #가져 올 수 없기 때문에 오류가 일어났다 if i==len=1 로 해결했다.

 # 2 런터임에러 dz=는 글자수가 3이다. dz일때 고려를 하지 않았다.



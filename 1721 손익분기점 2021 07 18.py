
a,b,c = map(int, input().split())
H = 0
while True:
    if b>= c:
        H= -1
        break
    else:
        H=int(a/(c-b))+1
        break

print(H)

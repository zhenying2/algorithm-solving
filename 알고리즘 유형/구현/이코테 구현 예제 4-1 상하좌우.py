#예제 4-1

N=int(input()) #공간의 크기
move=list(input().split())

x=1
y=1

for i in range(len(move)):
    if move[i] == 'L' : #왼쪽으로 한칸 이동
        if x !=1:
            x-=1
    elif move[i] == 'R': #오른쪽 한칸 이동
        if x != N:
            x+=1
    elif move[i] == 'U': #위쪽으로 한칸 이동
        if y != 1:
            y-=1
    elif move[i] == 'D': #아래로 한칸 이동
        if y !=N:
            y+=1

print(y,x)

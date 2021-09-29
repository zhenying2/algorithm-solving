#실전문제3 게임 개발

#N,M 입력
N,M=map(int,input().split())

#첫번째 사용자의 위치와 바라보는 방향
x,y,direction=map(int,input().split())

#맵의 육지/바다 상태 정보
infor=[]

#육지/바다의 정보 입력
for _ in range(N):
    info=list(map(int,input().split()))
    infor.append(info)

count=0 #방문한 칸 수를 세는 변
step=1 #방향 돌리는 횟수 세는 변수

infor[y][x]=-1 #현재 위치 방문한 걸로 생각하기 위해 -1로 바꿈

while True:
    if step !=5:
        #현재 방향 기준으로 왼쪽 방향부터 갈곳을 정한다.
        if direction ==0: #북쪽방향보고 있었다면,
            new_direction=3
            if infor[y][x-1] == 0:
                direction=new_direction
                save=direction
                infor[y][x-1]=-1
                x=x-1
                count+=1
                step=1
                continue
            else:
                save=direction
                direction=new_direction
                step+=1
                continue

        elif direction ==1: #동쪽방향보고 있었다면,
            new_direction=0
            if infor[y-1][x] == 0:
                direction=new_direction
                save=direction
                infor[y-1][x]=-1
                y=y-1
                count+=1
                step=1
                continue
            else:
                save=direction
                direction=new_direction
                step+=1
                continue

        elif direction ==2: #남쪽방향보고 있었다면,
            new_direction=1
            if infor[y][x+1] == 0:
                direction=new_direction
                save=direction
                infor[y][x+1]=-1
                x=x+1
                count+=1
                step=1
                continue
            else:
                save=direction
                direction=new_direction
                step+=1
                continue

        elif direction ==3: #서쪽방향 보고 있었다면,
            new_direction=2
            if infor[y+1][x] == 0:
                direction=new_direction
                save=direction
                infor[y+1][x]=-1
                y=y+1
                count+=1
                step=1
                continue
            else:
                save=direction
                direction=new_direction
                step+=1
                continue
            
    if step ==5:
        if direction==0: #기존 방향이 북쪽
            if infor[y+1][x] == 1: #뒤가 바다라면
                break
            else: #뒤쪽이 바다가 아니라면
                direction=save
                y+=1
                count+=1
                step=1
                continue                                  
        elif direction ==1: #기존 방향이 동쪽
            if infor[y][x-1] == 1:
                break
            else:
                direction=save
                x-=1
                count+=1
                step=1
                continue
                            
        elif direction ==2: #기존 방향이 남쪽
            if infor[y-1][x] == 1:
                break
            else:
                direction=save
                y-=1
                count+=1
                step=1
                continue
        elif direction==3: #기존 방향이 서쪽
            if infor[y][x+1] == 1:
                break
            else:
                direction=save
                x+=1
                count+=1
                step=1
                continue
            
print(count)
        

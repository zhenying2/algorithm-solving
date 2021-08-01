import sys

count=int(sys.stdin.readline().strip())

status=[]

#status 리스트안에 [x,y] 원소로 => 이중리스트 status 완성
for i in range(count):
    status.append(list(map(int,sys.stdin.readline().split(" "))))

#정렬 기준: 우선순위) y좌표 오름차순 -> x좌표 오름차순
#sort의 default는 오름차순이므로 reverse=False는 따로 안써줘도 무방
status.sort(key=lambda x: (x[1],x[0]))

for i in range(len(status)):
    for j in range(2):
        print(status[i][j], end=" ")
    print()
#정수 N, M을 입력받기
n,m=map(int,input().split())

#n개의 화폐 단위 정보를 입력받기
array=[]
for i in range(n):
    array.append(int(input()))

#한번 계산된 결과를 저장하기 위해 DP 테이블 초기화
#화폐 단위는 10,000 보다 작거나 같은 자연수
d=[10001]*(m+1)

#다이나믹 프로그래밍
d[0]=0
for i in range(n):
    for j in range(array[i],m+1):
        d[j]=min(d[j],d[j-array[i]]+1)

#계산 결과 출력
if d[m] == 10001: #M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])

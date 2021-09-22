#행과 열을 입력받음
n,m=map(int,input.split())

result=0

for i in range(n):
    data=list(map(int,input.split()))

    #현재 가장 작은 수 찾기
    minimum=min(data)

    #'가장 작은 수'들 중 가장 큰 값 찾기
    result=max(result,minimum)

print(result)

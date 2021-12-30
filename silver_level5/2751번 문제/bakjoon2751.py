#bakjoon 2751번
#2021.12.30

#반복되는 횟수 입력
N=int(input())

#전체 숫자 입력
num_origin=[]
for _ in range(N):
    temp=int(input())
    num_origin.append(temp)

#정렬된 결과 출력
num_origin.sort()
for i in range(N):
    print(num_origin[i])

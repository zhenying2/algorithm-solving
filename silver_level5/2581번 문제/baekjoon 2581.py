#baekjoon 2581
#2022.01.09

M=int(input())
N=int(input())

sum_list=[]
total=0
#M이상 N이하에서 소수 찾기
for i in range(M,N+1):
    not_error=True
    if (i==1):
        not_error=False
    if (i > 1):
        for j in range(2,i):
            if (i % j ==0): #i를 j로 나눴을 때 나머지 0 -> 소수 아님
                not_error=False
                break
        if (not_error): #not_error true-> 소수
            sum_list.append(i)
            total+=i

if (sum_list): #빈리스트가 아니라면
    print(total)
    print(sum_list[0])
else: #빈 리스트라면
    print(-1)
    

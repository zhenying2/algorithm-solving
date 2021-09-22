#N과 K의 입력
N,K=map(int,input.split())

#N이 1이 될때까지 1, 2 조건의 횟수 세는 변수
count=0

#N이 1이 될 때까지 반복해 수행
while N !=1:

    #N이 K로 나누어 떨어진다면 나눗셈 먼저 하는게 횟수가 적게 나옴
    if N % K ==0:
        count +=1
        N=N/K

    #N이 K로 나누어 떨어지지 않는다면
    else:
        count +=1
        N-=1

#N이 1이 되어 해당 프로그램 빠져 나왔다면,
print(count)
        

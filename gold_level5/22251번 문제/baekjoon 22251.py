#baekjoon 22251
#2022.01.08


def check(P,j):
    global count
    
    if P == 0 :
        count +=1
    else:
        for i in range(10):
            if (led[j][i] <=P):
                count+=1

    
#각 숫자에서 led 반전시키는 횟수
led=[[0,4,3,3,4,3,2,3,1,2],[4,0,5,3,2,5,6,1,5,4],[3,5,0,2,5,4,3,4,2,4],[3,3,2,0,3,2,3,2,2,1],[4,2,5,3,0,3,4,3,3,2]
     ,[3,5,4,2,3,0,1,4,2,1],[2,6,3,3,4,1,0,5,1,2],[3,1,4,2,3,4,5,0,4,3],[1,5,2,2,3,2,1,4,0,1],[2,4,4,1,2,1,2,3,1,0]]

#N층, 자리수K, 바꿀수 있는 횟수 P, 현재층X 
N, K, P, X=map(int,input().split())

#자리수 확인
#1자리수라면
if (K == 1):
    count=0 #바꿔서 표현할 수 있는 횟수 변수
    for i in range(10):
        if (i == X): #현재층이랑 같다면
            continue
        elif (i > N): # 건물의 최대 층보다 더 크다면
            break
        elif (led[X][i] <= P): #바꿀수 있는 횟수가 같거나 적다면
            count+=1

#2자리수라면
elif (K == 2):
    count=0 #바꿔서 표현할 수 있는 횟수 변수
    N1= N//10
    N2=N %10
    X1=P//10
    X2=P%10
    for i in range(10):
        if (i == N1): #건물의 십의 자리 숫자가 같다면
            for j in range(N2+1): #건물의 일의자리 숫자와 같거나 작을때동안
                if (j == X2): #현재 건물의 일의자리와 동일
                    continue
                elif (led[X1][j] <= P): #바꿀수 있는 횟수가 같거나 적다면
                    count+=1          
        elif (i > N1): # 건물의 십의자리 숫자보다 더 크다면
            break
        elif (i < N1): #건물의 십의 자리 숫자보다 작다면
            for k in range(10):
                if (i == X1 and k == X2): #현재 층과 동일
                    continue
                if (led[X1][k] < P):
                    tempP=P-led[X1][k]
                    check(tempP,X2)
                elif (led[X1][k] == P):
                    check(0,X2)
                                            
print(count)

            









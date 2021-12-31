#bakjoon 11653 소인수분해 문제
#2021.12.31
#최종 수정 풀이

#N 입력
N=int(input())

prime_number=2 #소수의 시작

while (N !=1):
    #N이 소수로 나눠떨어지는 경우 -> 소인수 분해 가능한 경우
    if (N % prime_number ==0):
        print(prime_number)
        N=N/prime_number

    #N이 소수로 나눠떨어지지 않는 경우
    else:
        prime_number+=1

        


    

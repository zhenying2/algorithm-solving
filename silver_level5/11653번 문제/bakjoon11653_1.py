#bakjoon 11653 소인수분해 문제
#2021.12.31
#처음 풀이

#N 입력
N=int(input())

prime_number=2 #소수의 시작

while (True):
    #N이 소수로 나눠떨어지는 경우 -> 소인수 분해 가능한 경우
    if (N % prime_number ==0):
        N=N/prime_number
        print(prime_number)
        continue

    #N이 소수로 나눠떨어지지 않는 경우
    else:
        #더하다가 소수가 1과 자기자신일 경우
        if (prime_number == N):
            print(N)
            break

        #자기 자신이 아닌경우
        prime_number+=1

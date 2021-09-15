# N, M ,K의 입력 (공백을 기준으로 나눔)
n, m, k=map(int,input().split())

#배열의 원소 입력 & 저장
a=list(map(int,input().split()))

a.sort() #a 배열의 분류

#배열의 가장 큰수, 가장 작은수 뽑기
first=a[-1]
second=a[-2]

result=0

if first == second:
	result= first*m

else:
    while True:
        for i in range(k):
            if m == 0:
                break
            result += first
            m -=1
		
        if m ==0:
            break
		
        result +=second
        m -=1
	
print(result)

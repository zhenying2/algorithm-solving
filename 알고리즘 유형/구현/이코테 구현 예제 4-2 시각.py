#예제 4-2

N=int(input()) #정수 N 시각 입력

count=0
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                count +=1

print(count)

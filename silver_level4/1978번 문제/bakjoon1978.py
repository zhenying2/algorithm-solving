#bakjoon 1978
#2022.01.02

#수의 개수 N, 원소 입력
N=int(input())
numbers=list(map(int,input().split()))

#소수 찾기
count=0
search_num=2
for i in numbers:
    #i가 1이라면
    if i == 1:
        continue
    
    while i >= search_num:
        result=i % search_num
        
        #같은수가 될때까지 나눠지는 수가 없음 -> 소수
        if i == search_num:
            search_num=2
            count+=1
            break
        
        #i가 search_num으로 나눠진다면 -> 소수 아님
        elif (result == 0 ):
            search_num=2
            break

        else:
            search_num+=1
        
print(count)
        
    

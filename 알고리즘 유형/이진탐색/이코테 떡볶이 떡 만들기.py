#떡 개수 N과 떡 길이 M
N,M=map(int,input().split())
print(N,M)
#떡의 개별 높이 입력
listA=list(map(int,input().split()))
listA.sort()
print(listA)

for i in listA:
    height=i
    sum=0
    
    if sum != M:
        for j in listA:
            if j<=height:
                temp=0
            else:
                temp=j-height
                
            sum+=temp
            
        if sum == M:    
            print(i)
            break

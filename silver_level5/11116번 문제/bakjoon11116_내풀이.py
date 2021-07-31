import sys

#테스트 케이스의 개수 입력
n=int(sys.stdin.readline().strip())

#테스트 케이스만큼 반복 수행
for _ in range(n):
    m=int(sys.stdin.readline().strip())
    left= list(map(int,sys.stdin.readline().split(' ')))
    right=list(map(int,sys.stdin.readline().split(' ')))

    count=0
    for i in range(m):
        
        if (left[i]+500) in left:
            if (left[i]+1000) in right:
                if  (left[i]+1500) in right:

                    #right 원소를 지워야 한다.. 
                    #left 원소 지우면 range때문에 index 오류 남
                    right.remove(left[i]+1000)
                    right.remove(left[i]+1500)

                    count+=1


    print(count)


    
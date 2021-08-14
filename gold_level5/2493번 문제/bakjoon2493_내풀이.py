#시간초과

import sys

#탑의 개수 입력
count=int(sys.stdin.readline().strip())

#탑의 길이 입력
tops=list(map(int,sys.stdin.readline().split()))

#수신하는 탑의 번호 확인 
for i in range(count):
    #첫번째 탑의 신호는 항상 수신못받음
    if i ==0:
        print(0, end=" ")

    elif i ==1:
        if tops[i] > tops[0]:
            print(0, end=" ")
        else:
            print(1, end=" ")
    
    else:
        for j in range(i-1,-1,-1):
            if tops[i] < tops[j] :
                print(j+1, end=" ")
                break
print()


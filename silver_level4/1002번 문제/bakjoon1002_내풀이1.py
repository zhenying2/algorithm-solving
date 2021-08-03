import sys

#테스트 케이스의 개수
case_count=int(sys.stdin.readline().strip())

#각 케이스마다 위치 수 출력
for _ in range(case_count):
    #케이스 입력 (x1,y1,r1,x2,y2,r2)순으로
    case=list(map(int,sys.stdin.readline().split(' ')))

    #원과의 교점 -> 두 중심간의 거리와 반지름의 비교
    #python에서 제곱의 표현 pow(a,b)=a**b=a의 b제곱
    #python에서 루트의 표현 a**(1/2) or math라이브러리의 sqrt 함수 사용
    #python에서 절댓값 -> abs 함수
    d_x=pow((case[0]-case[3]),2)
    d_y=pow((case[1]-case[4]),2)
    c_distance=(d_x+d_y)**(1/2)

    r_1=(case[2]+case[5]) #두 원의 반지름 합
    r_2=abs(case[2]-case[5]) #두 원의 반지름 차 절댓값
    
    #원이 일치하는 경우 (교점 무한)
    if (c_distance ==0 and r_2 == 0):
        print(-1)

    #원이 1개에서 접하는 경우 (외접 or 내접)
    elif (c_distance == r_1 or c_distance == r_2):
        print(1)
    
    #원이 2개의 교점을 가지는 경우
    elif (c_distance > r_2 and c_distance < r_1):
        print(2)
    
    #원 교점 0인 경우 (두 원이 안만남)
    else:
        print(0)
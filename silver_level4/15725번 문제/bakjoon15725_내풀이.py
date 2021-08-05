import sys

#최대 일차 일변수 다항식 입력받음
fx=sys.stdin.readline().strip()

#x를 기준으로 나눔
#일차 일변수 다항식이기 때문에 가능한 것임

#x가 fx에 없다면
if (fx.find('x') == -1): #find했을 때 존재하지 않으면 -1을 default로 출력함
    print(0)

#x가 fx에 있다면
else:
    fx2=fx.split('x')

    #계수가 1인경우
    if (fx2[0] == ''):
        print(1)

    #계수가 -1인 경우
    elif (fx2[0] == '-'):
        print(-1)

    #계수가 1, -1이 아닌경우    
    else:
        print(int(fx2[0]))

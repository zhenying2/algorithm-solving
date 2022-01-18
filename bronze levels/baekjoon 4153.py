#baekjoon 4153
#2022.01.18
#bronze level 3

while (True):
    right_triangle=list(map(int,input().split()))
    right_triangle.sort() #작 -> 큰 순으로 정렬

    #000으로 입력 -> 테스트 종료
    if (right_triangle[0] == 0 and right_triangle[1] == 0 and right_triangle[2] == 0):
        break

    # 직각삼각형이라면
    elif (right_triangle[0]**2 + right_triangle[1]**2 == right_triangle[2]**2):
        print("right")

    #직각삼각형 아니라면
    else:
        print("wrong")

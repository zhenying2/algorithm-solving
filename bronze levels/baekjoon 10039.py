#baekjoon 10039
#2022.01.12
#bronze level 4

#5명 총점 담는 변수
total=0

for _ in range(5):
    score=int(input())

    #만약 점수가 40점 이상이라면,
    if score >= 40:
        total+=score

    #점수 40점 미만이라면
    else:
        total+=40

#평균 출력
print(int(total/5))

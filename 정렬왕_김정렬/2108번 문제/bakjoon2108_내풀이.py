#백준_정렬왕
#문제: 2108번 내 풀이

#최빈값을 구하기 위한 모듈 사용
from collections import Counter

size=int(input())

#입력값 받기와 각 자료 리스트에 저장과정
arrayA=[]

for i in range(size):
    i=i+1
    arrayA.append(int(input()))    

arrayA.sort()
print(arrayA)

#1. 산술평균 출력
sum=0
for a in arrayA:
    sum=a+sum

#round(실수, n)은 실수를 소수점 이하 n자리까지만 표현하고 싶을 때 사용함
print(round(sum/size))


#2. 중앙값 출력
#size값은 문제에서 홀수라 가정됨
index=round(size/2)
#기존 홀수 중앙값으 +1시켜줘야 하나, 인덱스 값이 0부터 시작하므로 +1작업을 안해도 무방
print(arrayA[index])

#3. 최빈값 출력
countsmode=Counter(arrayA).most_common()
#원소가 여러개로 최빈값 비교 가능한 경우
if len(countsmode) > 1:
    #최빈값이 여러개로 동일한 경우 2번째 값으로 출력
    if countsmode[0][1] == countsmode[1][1]:
        print(countsmode[1][0])
    #최빈값 1개인 경우 1번째 값으로 출력
    else:
        print(countsmode[0][0])
#원소가 한개로 최빈값 비교 불가능하므로 1번째 값 그냥 출력        
else:
    print(countsmode[0][0])

#4. 범위 출력
print(arrayA[size-1]-arrayA[0])
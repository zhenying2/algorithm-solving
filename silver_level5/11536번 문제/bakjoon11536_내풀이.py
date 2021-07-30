import sys


number=int(sys.stdin.readline().strip())

names=[]

for _ in range(number):
    people=sys.stdin.readline().strip()
    names.append(people)

#sort는 대문자 -> 소문자 순으로 정렬 기본값
#sort는 기존리스트 정렬만, 새로운 변수는 sort로 할당 불가 (none으로 출력)
upnames=sorted(names)
downnames=sorted(names, reverse=True)

#정렬 순서 비교 (파이썬 리스트 원소 비교가 비교연산자 한방에 되다니.. 너무 편리하다)
if (names == upnames):
    print("INCREASING")
elif (names == downnames):
    print("DECREASING")
else:
    print("NEITHER")
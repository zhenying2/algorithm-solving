#baekjoon 11931
#2022.01.22
#silver 5 level

import sys
input=sys.stdin.readline

#N개의 수 입력할 것이다.
N=int(input())

#내림차순 정렬하기
numbers=[]
for _ in range(N):
  temp=int(input())
  numbers.append(temp)

numbers.sort(reverse=True)

#내림차순 정렬 출력
for i in numbers:
  print(i)
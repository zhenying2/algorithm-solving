#baekjoon 14889
#2022.01.27
#silver level 3

import sys
from itertools import combinations
input=sys.stdin.readline

#팀원 N명 입력
N=int(input().rstrip())
skills=[]
for i in range(N):
  skills.append(list(map(int,input().rstrip().split())))

#n/2 쌍 나누기
#초기화
standard=[i for i in range(N)]
pair1=list(combinations(standard,int(N/2)))
pair2=[]
#different 차이 저장
diff=[]
for i in range(len(pair1)):
  pair2.append(list(set(standard)-set(pair1[i])))
  s1=0
  s2=0
  for j in range(int(N/2)-1):
    for k in range(j+1,int(N/2)):
      s1+=skills[pair1[i][j]][pair1[i][k]]+skills[pair1[i][k]][pair1[i][j]]
      s2+=skills[pair2[i][j]][pair2[i][k]]+skills[pair2[i][k]][pair2[i][j]]
  diff.append(int(abs(s1-s2)))

print(min(diff))



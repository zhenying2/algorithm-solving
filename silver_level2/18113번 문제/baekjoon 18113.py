#baekjoon 18113
#2022.02.10
#문제 이해가 잘 안되는 부분 (한쪽만 꼬다리자른 경우..?)
#일단 내가 문제 이해한대로 작성
#silver level 2

#김밥개수N, 꼬다리길이K, 김밥조각 최소개수M
import sys
input=sys.stdin.readline
N,K,M=map(int,input().split())
result=[]
for i in range(N):
  kimbab_length=int(input())
  if (kimbab_length>2*K):
    kimbab_length-=2*K
    result.append(int(kimbab_length//M))
  elif (kimbab_length==2*K):
    continue
  else: #kimbab_length<2*K
    if (kimbab_length==K or kimbab_length<K):
      continue
    else:
      kimbab_length-=(K+1)
      result.append(int(kimbab_length//M))

if (result):
  print(max(result))
else:
  print(-1)
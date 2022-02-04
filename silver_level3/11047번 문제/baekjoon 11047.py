#2022.02.04
#baekjoon 11047
#silver level 3
import sys
input=sys.stdin.readline
N,K=map(int,input().rstrip().split())
CoinValue=[]
coins=0

#동전 가치 입력
for _ in range(N):
  CoinValue.append(int(input().rstrip()))

#동전 개수 최소값 찾기
while True:
  if (K==0):
    print(coins)
    break

  for j in range(N):
    if (K < CoinValue[j]):
      temp=int(K//CoinValue[j-1])
      coins+=temp
      K-=int(CoinValue[j-1]*temp)
      break



#bakjoon 1631
#2022.01.03

#디스크 개수 N과 움직이는 횟수 M
N,M=map(int,input().split())

#원하는 결과의 형태 -> 리스트에 넣기
str_result=input()
list_result=[]
for i in range(N):
    list_result.append(str_result[i])


count=0 #움직이는 횟수 세는 변수
while (count != M):
        f(N,"A",list_result[N-count])
    
    

def f(n, a, b):
  if(n == 1):
    count+=1 #count 수 증가
  else:
    f(n-1, "A","B")
    f(1, "A", "C")
    f(n-1, "B", "C")

n = int(input())
print(2**n-1)
if(n <= 20):
  f(n, 1, 2, 3)

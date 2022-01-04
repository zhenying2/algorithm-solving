#bakjoon 1631
#2022.01.03, 01.04

#디스크 개수 N과 움직이는 횟수 M
N,M=map(int,input().split())

#원하는 결과의 형태 -> 리스트에 넣기
str_result=input()
list_result=[]
for i in range(N):
    list_result.append(str_result[i])


count=0 #움직이는 횟수 세는 변수
#최종 결과 저장 리스트    
final_result=[]
for _ in range(N):
    final_result.append("A")
print(final_result)  
def f(n, a, b, c):
  if(n == 1):
    global count
    global final_result
    #final_result[count]=c         <- 이부분 수정 필요.....
    count+=1 #count 수 증가
    print(final_result)
    print(count)
    print(n)
  else:
    f(n-1, a,c,b)
    f(1, a, b,c)
    f(n-1, b,a,c)
    
while (count != M):
    if (list_result[N-1-count] == "B"):
        f(N,"A","C","B")
    elif (list_result[N-1-count] == "C"):
        f(N,"A","B","C")
    else:
        copy_N=N
        while (list_result[N-1-count] !="A"):
            copy_N-=1
        if (list_result[copy_N-1-count] =="B"):
            f(copy_N,"A","C","B")
        elif (list_result[N-1-count] == "C"):
            f(copy_N,"A","B","C")
        
        

#결과 출력        
if (M == 0 ):
    print("A"*N)
else:
    for i in range(N):
        print(final_result[i],end="")



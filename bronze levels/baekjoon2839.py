#baekjoon 2839
#2022.01.10

N=int(input())

bongji1=[]
range5=int(N//5)
bongji2=[]
range3=int(N//3)

#5를 기준으로 3
for i in range(range5+1):
    for j in range(range3+1):
        if (N == (i*5+j*3)):
            bongji1.append(i+j)
            break

#3을 기준으로 5
for i in range(range3+1):
    for j in range(range5+1):
        if (N == (i*3+j*5)):
            bongji2.append(i+j)
            break        

#bongji1과 bongji2 정렬 (작 -> 큰 순으로)
bongji1.sort()
bongji2.sort()

#빈 리스트 확인 -> 제거
if (not bongji1): #bongji1이 빈리스트라면
    bongji1.append(0)
if (not bongji2): #bongji2이 빈리스트라면
    bongji2.append(0)

if (bongji1[0] == 0 and bongji2[0] == 0 ) : #N에 맞는 최소 봉지수 찾을 수 없는 경우
    print(-1)
elif (bongji1[0]>0 and bongji1[0] <= bongji2[0]): #bongji1의 봉지수가 더 적거나 같다면
    print(bongji1[0])
elif (bongji2[0]>0 and bongji1[0] > bongji2[0]): #bongji2의 봉지수가 더 적다면
    print(bongji2[0])

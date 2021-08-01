import sys

count=int(sys.stdin.readline().strip())

time=list(map(int,sys.stdin.readline().split()))

time.sort()

total_time=[]



for i in range(count):
    #1번째 사람의 시간 total_time 리스트 원소로 추가
    #자기 자신의 시간만 원소로 추가
    if i == 0:
        total_time.append(time[i])

    #1번째 사람의 시간 total_time 리스트 원소로 추가
    #이전의 원소 시간의 합을 구해서 원소로 추가
    else:
        total_time.append(time[i]+total_time[i-1])


#리스트 원소의 합 => sum 함수로 한방에 가능
print(sum(total_time))
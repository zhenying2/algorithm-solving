import sys

#N장의 카드의 N값을 입력받음
count=int(sys.stdin.readline().strip())

#N개의 번호 numbers 리스트에 저장
numbers=[]
for i in range(1, count+1):
    numbers.append(i)
    
#홀수번 시도 -> 맨위 수 버리기
#짝수번 시도 -> 맨위 수 가장 아래로 이동

i=1 #시도 세는 변수
while True:
    # numbers에 원소가 1개 남을때까지 반복
    if (len(numbers) != 1):
        #홀수번 시도일 경우
        if (i % 2 == 1):
            i+=1
            del numbers[0] #가장 위 수 버리기
            
        #짝수번 시도일 경우
        else:
            i+=1
            move=numbers[0]
            del numbers[0] #가장 위 수 버리고
            numbers.append(move) #그 수를 맨 뒤로 이동시킨다.

    # numbers에 원소 1개라면 (입력 n이 항상 1보다는 크므로)
    else: 
        print(numbers[0])
        break
            




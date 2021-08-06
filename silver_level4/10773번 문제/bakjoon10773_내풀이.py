import sys

#반복해서 입력받을 횟수 입력
count=int(sys.stdin.readline())

save=[]
for _ in range(count):
    sample=int(sys.stdin.readline())

    #입력한 수 0 -> 가장 마지막 수 삭제
    if (sample == 0 ):
        del save[len(save)-1]
    
    #입력한 수 0이 아니라면
    else:
        save.append(sample)

#총합 출력
sum=0
for i in range(len(save)):
    sum+=save[i]

print(sum)
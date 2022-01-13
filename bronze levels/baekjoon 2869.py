#baekjoon 2869
#2022.01.13
#bronze level 1
#반복문 사용 -> timeover

A,B,V=map(int,input().split())

i=1
count=1
distance=0
    
while True:
    #(낮 기준) 달팽이 올라간 거리 >= 나무막대라면
    if (distance+A >= V):
        print(count)
        break

    #(낮에 기준 충족 X -> 밤에 미끄러짐)
    else:
        distance=(A-B)*i
        count+=1
        i+=1
        continue
        
        
        

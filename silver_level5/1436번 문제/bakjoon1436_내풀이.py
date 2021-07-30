n = int(input()) 
num = 666 
count = 0 #n과 비교할 변수(숫자)

while True:
    #num 문자열에 666이 있을때
    if "666" in str(num): 
        count += 1 
    
    #더한 카운트와 입력값이 같을때
    if count == n: 
        print(num) 
        break

    #num에 666이 없을때
    num += 1 


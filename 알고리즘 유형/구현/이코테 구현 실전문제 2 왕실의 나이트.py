#실전문제2 왕실의 나이트

#현재 나이트의 위치 파악
where=input()
x=where[0]
y=int(where[1])

count=0

#오2위1
if x != 'g' and x !='h' and y !=1:
    count +=1
    
#오2아래1
if x != 'g' and x !='h' and y !=8:
    count +=1
    
#왼2위1
if x != 'a' and x !='b' and y !=1:
    count +=1

#왼2아래1
if x != 'a' and x !='b' and y !=8:
    count +=1

#아래2오1
if x != 'h' and y !=7 and y !=8:
    count +=1

#아래2왼1
if x != 'a' and y !=7 and y !=8:
    count +=1
    
#위2오1
if x != 'h' and y !=1 and y !=2:
    count +=1
    
#위2왼1
if x != 'a' and y !=1 and y !=2:
    count +=1

print(count)

#거슬러 줘야 하는 돈이 1260원 일때,

n=1260
count=0

#큰 단위 화폐부터 차례대로 확인
coin_types=[500,100,50,10]

for coin in coin_types:
	count += n//coin #해당 화폐로 거슬러 줄 수 있는 동적의 개수 세기
	n %= coin 

print(count)

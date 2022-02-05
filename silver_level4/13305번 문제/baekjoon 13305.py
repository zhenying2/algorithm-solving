#baekjoon 13305
#2022.02.06
#silver level 4

n = int(input())
road_len = list(map(int, input().split()))
city_price = list(map(int, input().split()))

res = 0
price = city_price[0]
for i in range(n - 1):
    if i > 0 and city_price[i] < price:
        price = city_price[i]
    res += road_len[i] * price

print(res)
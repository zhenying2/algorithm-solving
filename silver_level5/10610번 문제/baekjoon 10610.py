#baekjoon 10610
#2022.01.23
#silver level 5

N=input()
lists=list(N)
numbers=list(map(int,lists))
#내림차순으로 정렬
numbers.sort(reverse=True)
sum=0
for i in numbers:
  sum+=i
#30=2*3*5
#입력한 수에 0이 있다면, 2와 5의 배수 만족
if numbers[-1] == 0:
  #3의 배수라면(=자리수의 합이 3의 배수)
  if sum % 3 ==0:
    lists.sort(reverse=True)
    str_result=""
    for i in lists:
      str_result+=i
    int_result=int(str_result)
    print(int_result)
  else: #3의 배수가 아님
    print(-1)
else:
  print(-1)



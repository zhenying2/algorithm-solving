#baekjoon 9095
#2022.01.31
#silver level 3

testcase=int(input())
 
dp=[ 0 for i in range(12)]
 
dp[1]=1
dp[2]=2
dp[3]=4
 
for i in range(4,12):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
 
for i in range(testcase):
    a=int(input())
    print(dp[a])
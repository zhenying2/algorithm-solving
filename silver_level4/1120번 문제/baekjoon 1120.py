#baekjoon 1120
#2022.01.28
#silver level4

a,b=input().split()
limit=len(b)-len(a)
diff=[]
for i in range(limit+1):
  count=0
  standard=b[i:len(a)+i]
  for j in range(len(a)):
    if (a[j] != standard[j]):
      count+=1
  diff.append(count)

print(min(diff))


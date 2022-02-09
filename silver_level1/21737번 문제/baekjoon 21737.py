#baekjoon 21737
#2022.02.09
#silver level1
N=int(input())
inputs=input()
formula=[]
string=""
for i in range(len(inputs)):
  if (inputs[i]=='S'):
    if (string):
      formula.append(int(string))
      string=""
    formula.append('S')
  elif(inputs[i]=='M'):
    if (string):
      formula.append(int(string))
      string=""
    formula.append('M')
  elif(inputs[i]=='U'):
    if (string):
      formula.append(int(string))
      string=""
    formula.append('U')
  elif(inputs[i]=='P'):
    if (string):
      formula.append(int(string))
      string=""
    formula.append('P')
  elif(inputs[i]=='C'):
    if (string):
      formula.append(int(string))
      string=""
    formula.append('C')
  else:
    string+=inputs[i]
result=formula[0]
if 'C' in formula:
  for i in range(1,len(formula)):
    if (formula[i]=='S'):
      if (i==len(formula)-1):
        break
      result=result-formula[i+1]
    elif (formula[i]=='M'):
      if (i==len(formula)-1):
        break
      result=result*formula[i+1]
    elif (formula[i]=='U'):
      if (i==len(formula)-1):
        break
      if (result>=0):
        result=result//formula[i+1]
      else: #음수
        result=-1*((-1*result)//formula[i+1])
    elif (formula[i]=='P'):
      if (i==len(formula)-1):
        break
      result=result+formula[i+1]
    elif (formula[i]=='C'):
      print(result, end=" ") 
else:
  print('NO OUTPUT')

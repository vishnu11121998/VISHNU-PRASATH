n=int(input())
print(n,end=",")
for i in range(n):
  a=n*3
  b=a+1
  print(str(a)+","+str(b),end=",")
  n=b
  a=b
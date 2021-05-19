#program to print add series
#20,16,13,9,6,2


n=int(input())
print(n,end=",")
for i in range(n):
  a=n-4
  b=a-3
  print(str(a)+","+str(b),end=",")
  n=b
  a=b


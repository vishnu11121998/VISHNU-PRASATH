n=int(input())
sum=0
for i in range(n,2,-2):
  sum=sum+i
  print(i,end="+")
print(str(i-2)+"="+str(sum+2))



#pattern 56
 # 1
 # 2 6
 # 3 7 10
 # 4 8 11 13
 #



n=5
for i in range(1,n+1):
  x=i
  for j in range(1,i+1):
    print(str(x)+"",end=" ")
    x=x+(n-j)
  print("")
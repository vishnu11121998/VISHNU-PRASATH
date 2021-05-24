#pattern 44
 # 1
 # 3 2
 # 6 5 4
 # 10 9 8 7


x=0
for i in range(1,5):
  x+=i
  for j in range(x,x-i,-1):
    print(str(j)+"",end=" ")
  print("")
#pattern 55
 # 1
 # 4 9
 # 16 25 36
 # 49 64 81 100



x=1
for i in range(1,5):
  for j in range(1,i+1):
    print((x*x),end=" ")
    x+=1
  print("")
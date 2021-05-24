#pattern 46
 # 2
 # 4 6
 # 8 10 12
 # 14 16 18 20
 # 22 24 26 28 30


x=2
for i in range(5,0,-1):
  for j in range(6,i,-1):
    print(x,end=" ")
    x += 2
  print("")
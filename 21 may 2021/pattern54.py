#pattern 54
 # 1
 # 1 2
 # 2 3 4
 # 4 5 6 7 
 # 7 8 9 10 11



x=1
for i in range(5):
  for j in range(0,i+1):
    print(x-i,end=" ")
    x+=1
  print("")
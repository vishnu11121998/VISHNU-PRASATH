# pattern 25

 #  1 0 1 0 1
 #  1 0 1 0 1
 #  1 0 1 0 1
 #  1 0 1 0 1
 #  1 0 1 0 1

n=5
for i in range(1,n+1):
  for j in range(1,n+1):
    print(str(j%2)+"",end=" ")
  print("")
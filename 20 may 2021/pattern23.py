# pattern 23

 #  1 1 1 1 1
 #  0 0 0 0 0
 #  1 1 1 1 1
 #  0 0 0 0 0
 #  1 1 1 1 1

n=5
for i in range(1,n+1):
  for j in range(0,n):
    print(str(i%2)+"",end=" ")
  print("")
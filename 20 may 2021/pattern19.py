# pattern 19

 #  1 0 1 0 1
 #  0 1 0 1 0
 #  1 0 1 0 1
 #  0 1 0 1 0
 #  1 0 1 0 1




n=5

for i in range(1,n+1):
  for j in range(0,n):
    print(str((i+j)%2)+"",end=" ")
  print("")
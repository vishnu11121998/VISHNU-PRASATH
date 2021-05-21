# pattern 24

 #  0 1 0 1 0
 #  0 1 0 1 0
 #  0 1 0 1 0
 #  0 1 0 1 0
 #  0 1 0 1 0

n=5
for i in range(0,n):
  for j in range(0,n):
    print(str(j%2)+"",end=" ")
  print("")
#  pattern 41
 
#  1
#  2 3
#  4 5 6
#  7 8 9 10


n=1
for i in range(1,4):
  for j in range(1,i+1):
    print(str(n)+"",end=" ")
    n+=1
  print("")
#  pattern 42
 
#  1
#  2 3
#  3 4 5 
#  4 5 6 7 
#  5 6 7 8 9


for i in range(1,6):
  for j in range(1,i+1):
    print((i+j-1),end=" ")
  print("")
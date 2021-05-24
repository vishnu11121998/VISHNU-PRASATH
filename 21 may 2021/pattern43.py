#  pattern 43

 
#  1
#  3 5 
#  5 7 9 
#  7 9 11 13
#  9 11 13 15 17


for i in range(1,6):
  x=i-1
  for j in range(1,i+1):
    print((x+i),end=" ")
    x+=2
  print("")
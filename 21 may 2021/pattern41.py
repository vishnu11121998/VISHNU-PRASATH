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
  
  
  #   i      j        print      n+=1 
  
  #   1    (1,2)T      1           2
  #   2    (1,3)T      2           3   
  #   2    (1,3)T      3           4
  #   3    (1,4)T      4           5
  #   3    (1,4)T      5           6
  #   3    (1,4)T      6           7  
  #   4    (1,5)T      7           8
  #   4    (1,5)T      8           9
  #   4    (1,5)T      9           10
  #   4    (1,5)T     10           
  

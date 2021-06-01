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
  
  
  #   i      j       j(val)     print      n+=1 
  
  #   1    (1,2)T      1          1           2
  #   2    (1,3)T      1          2           3   
  #   2    (1,3)T      2          3           4
  #   3    (1,4)T      1          4           5
  #   3    (1,4)T      2          5           6
  #   3    (1,4)T      3          6           7  
  #   4    (1,5)T      1          7           8
  #   4    (1,5)T      2          8           9
  #   4    (1,5)T      3          9           10
  #   4    (1,5)T      4         10           
  

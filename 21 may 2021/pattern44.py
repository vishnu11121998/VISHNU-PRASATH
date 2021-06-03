#pattern 44
 # 1
 # 3 2
 # 6 5 4
 # 10 9 8 7


x=0
for i in range(1,5):
  x+=i
  for j in range(x,x-i,-1):
    print(str(j)+"",end=" ")
  print("")
  
  
  
#   i        x          j             print
#   1        1        (1,0)             1
#   2        3        (3,1)             3
             3        (2,1)             2
 #  3        6        (6,3)             6
             6        (5,3)             5
             6        (4,3)             4
 #  4        10       (10,6)           10
             10       (9,6)             9
             10       (8,6)             8
             10       (7,6)             7

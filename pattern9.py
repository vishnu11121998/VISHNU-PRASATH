# pattern 9

#    1  2  3  4   5
#    2  4  6  8  10
#    3  6  9 12  15
#    4  8 12 16  20
#    5 10 15 20  25

res=1
for i in range(1,6):
  for j in range(1,6):
    if i>0:
     print(" ",(i*j),end=" ")
    elif j<1:
     print(i*j,end=" ")
    else:
     print(str(res),end=" ")
     res+=2
  print("")

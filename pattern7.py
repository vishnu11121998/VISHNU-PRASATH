# pattern 7

#    1  3  5  7  9
#   11 13 15 17 19
#   21 23 25 27 29
#   31 33 35 37 39
#   41 43 45 47 49

res=1
for i in range(1,6):
  for j in range(1,6):
    if i<1:
     print(" ",(i*j),end=" ")
    elif j<1:
     print(i*j,end=" ")
    else:
     print(str(res),end=" ")
     res+=2
  print("")

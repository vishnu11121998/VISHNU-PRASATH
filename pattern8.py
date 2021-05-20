#       pattern 8
#      2  4  6  8 10
#     12 14 16 18 20
#     22 24 26 28 30
#     32 34 36 38 40
#     42 44 46 48 50


res=2
for i in range(1,6):
  for j in range(1,6):
    if i<1:
      print(i,str(res),end=" ")
    else:
      print(" "+str(res),end="")
      res += 2
  print("")
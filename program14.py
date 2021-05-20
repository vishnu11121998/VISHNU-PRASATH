n=5
for i in range(1,6):
  p=n-i+1
  for j in range(1,6):
    if i<2:
      print(""+str(p),end=" ")
    elif j<5:
        print(str(p),end=" ")
    else:
      print(str(p),end="")
    p=p+n
  print("")
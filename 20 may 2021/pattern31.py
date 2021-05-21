# pattern 31

 #  A B C D E
 #  B C D E F
 #  C D E F G
 #  D E F G H
 #  E F G H Y 

crc=0
for i in range(0,5):
  for j in range(0,5):
    print(chr(i+j+65)+"",end=" ")
    if crc<26:
     crc+=1
    else:
     crc=0
  print("")
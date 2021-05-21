# pattern 30

 #  A B C D E
 #  F G H I J
 #  K L M N O
 #  P Q R S T
 #  U V W X Y 

crc=0
for i in range(1,6):
  for j in range(1,6):
    print(chr(crc+65)+"",end=" ")
    if crc<26:
     crc+=1
    else:
     crc=0
  print("")
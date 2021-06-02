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
  
  
  #crc=0
  #    i       j        chr(crc+65)     if crc<26        crc=crc+1
  
  #    1       1         A                T                 crc=1  
  #    1       2         B                T                 crc=1  
  #    1       3         C                T                 crc=1  
  #    1       4         D                T                 crc=1  
  #    1       5         E                T                 crc=1    
  #    2       1         F                T                 crc=1   
  #    2       2         G                T                 crc=1   
  #    2       3         H                T                 crc=1  
  #    2       4         I                T                 crc=1  
  #    2       5         J                T                 crc=1  
  #    3       1         K                T                 crc=1  
  #    3       2         L                T                 crc=1  
  #    3       3         M                T                 crc=1    
  #    3       4         N                T                 crc=1   
  #    3       5         O                T                 crc=1   
  #    4       1         P                T                 crc=1  
  #    4       2         Q                T                 crc=1  
  #    4       3         R                T                 crc=1  
  #    4       4         S                T                 crc=1  
  #    4       5         T                T                 crc=1  
  #    5       1         U                T                 crc=1  
  #    5       2         V                T                 crc=1    
  #    5       3         W                T                 crc=1   
  #    5       4         X                T                 crc=1   
  #    5       5         Y                F                 crC=0  
  

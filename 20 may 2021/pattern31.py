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
  
  
  #crc=0
  #    i       j        chr(crc+65)     if crc<26        crc=crc+1
  
  #    0       0         A                T                 crc=1  
  #    0       1         B                T                 crc=1  
  #    0       2         C                T                 crc=1  
  #    0       3         D                T                 crc=1  
  #    0       4         E                T                 crc=1    
  #    1       0         B                T                 crc=1   
  #    1       1         C                T                 crc=1   
  #    1       2         D                T                 crc=1  
  #    1       3         E                T                 crc=1  
  #    1       4         F                T                 crc=1  
  #    2       0         C                T                 crc=1  
  #    2       1         D                T                 crc=1  
  #    2       2         E                T                 crc=1    
  #    2       3         F                T                 crc=1   
  #    2       4         G                T                 crc=1   
  #    3       0         D                T                 crc=1  
  #    3       1         E                T                 crc=1  
  #    3       2         F                T                 crc=1  
  #    3       3         G                T                 crc=1  
  #    3       4         H                T                 crc=1  
  #    4       0         E                T                 crc=1  
  #    4       1         F                T                 crc=1    
  #    4       2         G                T                 crc=1   
  #    4       3         H                T                 crc=1   
  #    4       4         I                F                 crC=0  
  

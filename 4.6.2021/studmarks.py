a=['16TH0321','Vishnu Prasath',92,93,94,89,90]
b=['16TH0365','JD',22,97,57,67,97]
c=['16TH0344','Master',96,65,89,65,50]
d=['16TH0324','Bigileyyyyy',20,23,43,13,76]
e=['16TH0367','Sarkar',91,88,47,75,90]
x=input("Enter the register number:")
print()
if(x==a[0]):
  print("Name of the student:",a[1])
  print("Tam=",a[2])
  print("Eng=",a[3])
  print("Mat=",a[4])
  print("Sci=",a[5])
  print("Soc=",a[6])
  print()
  t1=a[2]+a[3]+a[4]+a[5]+a[6]
  print("Total=",t1)
  if(t1>175):
   print("Result is pass")
  else:
   print("Result is fail")
elif(x==b[0]):
    print("Name of the student:",b[1])
    print("Tam=",b[2])
    print("Eng=",b[3])
    print("Mat=",b[4])
    print("Sci=",b[5])
    print("Soc=",b[6])
    print()
    t2=b[2]+b[3]+b[4]+b[5]+b[6]
    print("Total=",t2)
    if(t2>175):
     print("Result is pass")
    else:
     print("Result is fail")
elif(x==c[0]):
    print("Name of the student:",c[1])
    print("Tam=",c[2])
    print("Eng=",c[3])
    print("Mat=",c[4])
    print("Sci=",c[5])
    print("Soc=",c[6])
    print()
    t3=c[2]+c[3]+c[4]+c[5]+c[6]
    print("Total=",t3)
    if(t3>175):
     print("Result is pass")
    else:
     print("Result is fail")
elif(x==d[0]):
    print("Name of the student:",d[1])
    print("Tam=",d[2])
    print("Eng=",d[3])
    print("Mat=",d[4])
    print("Sci=",d[5])
    print("Soc=",d[6])
    print()
    t4=d[2]+d[3]+d[4]+d[5]+d[6]
    print("Total=",t4)
    if(t4>175):
     print("Result is pass")
    else:
     print("Result is fail")
elif(x==e[0]):
    print("Name of the student:",e[1])
    print("Tam=",e[2])
    print("Eng=",e[3])
    print("Mat=",e[4])
    print("Sci=",e[5])
    print("Soc=",e[6])
    print()
    t5=a[2]+a[3]+a[4]+a[5]+a[6]
    print("Total=",t5)
    if(t5>175):
     print("Result is pass")
    else:
     print("Result is fail")
else:
 print("Invalid")


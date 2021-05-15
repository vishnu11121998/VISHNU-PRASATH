Tam=int(input("Enter Tamil mark:"))
Eng=int(input("Enter English mark:"))
Mat=int(input("Enter Maths mark:"))
Sci=int(input("Enter Science mark:"))
Soc=int(input("Enter Social mark:"))
count=0
if Tam>=35:
  print("Cleared the exam")
else:
  print("Not cleared the exam")
  count=count+1
if Eng>=35:
  print("Cleared the exam")
else:
  print("Not cleared the exam")
  count=count+1
if Mat>=35:
  print("Cleared the exam")
else:
  print("Not cleared the exam")
  count=count+1
if Sci>=35:
  print("Cleared the exam")
else:
   print("Not cleared the exam")
   count=count+1
if Soc>=35:
  print("Cleared the exam")
else:
   print("Not cleared the exam")
   count=count+1
print("No of subjects failed:",count)
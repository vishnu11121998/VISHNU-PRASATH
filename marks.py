Tam=int(input("Enter Tamil mark:"))
Eng=int(input("Enter English mark:"))
Mat=int(input("Enter Maths mark:"))
Sci=int(input("Enter Science mark:"))
Soc=int(input("Enter Social mark:"))
count=count+1
if Tam>=35:
  if Eng>=35:
    if Mat>=35:
      if Sci>=35:
        if Soc>=35:
          print("Cleared the exam")
        else:
            print("Not cleared the exam")
            count=count+1
      else:
          print("Not cleared the exam")
          count=count+1
    else:
        print("Not cleared the exam")
        count=count+1
  else:
      print("Not cleared the exam")
      count=count+1
else:
    print("Not cleared the exam")
    count=count+1
print("No of subjects failed:",count)




  
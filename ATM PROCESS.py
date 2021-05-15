print("*****ATM WITHDRW PROCESS*****\n")
print("INSERT THE CARD\n")
Language=str(input("Enter Language:"))
if Language=="English" or Language =="French" or Language =="Tamil":
  print("Language selected\n")
Pin=int(input("Enter PIN number:"))
b = str(Pin)
l = len(b)
if l==4:
  print("Valid\n")
else:
    print("Invalid\n")
Trans=str(input("Select type of Transaction:"))
if Trans=="Deposit" or Trans=="Withdraw":
  print("Valid\n")
else:
  print("Invalid\n")
Account=str(input("Select type of account:"))
if Account=="Savings" or Account=="Current":
 print("Valid\n")
else:
  print("Invalid\n")
Amount=int(input("Enter the amount:"))
print("TRANSACTION PROCESSES......\n")
Totalamt=25000
currentbalance=Totalamt-Amount
print("currentbalance=",currentbalance)
print("\n")
print("TAKE THE CASH FROM BELOW\n")
print("Pls remove the card\n")
print("*****THANK U VISIT US AGAIN******")




    
 
 

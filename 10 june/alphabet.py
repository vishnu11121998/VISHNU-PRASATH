#accept only alpha
ch = input("Enter name: ")
a=ch.isalpha()
if a==False:
 print("Enter the name :")
else:
 print("Welcome ",ch)

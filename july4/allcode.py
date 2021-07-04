print("1.To perform (a+b)^2")
print("2.capital letter on both ends of string")
print("3.factorial of a given number")
print("4.head or tail game")
print("5.Longest string in a sentence")
print("6.Multiply table")
print("7.shopping cart")
print("8.signin and signout program")
print("9.square using functions")
print("10.Sum of digits")
print("11.Tictoe game")
print("12.upper and lower case")
print("13.Welcome name message program")
choice = int(input("Enter the code to perform:"))
if choice == 1:
    from upload.basiccalc import *
elif choice == 2:
    from upload.capsonbothsides import *
elif choice == 3:
    from upload.factorial import *
elif choice == 4:
    from upload.headortail import *
elif choice == 5:
   from upload.longestt import *
elif choice == 6:
    from upload.multiplytable import *
elif choice == 7:
    from upload.shopping import *
elif choice == 8:
    from upload.signinsignout import *
elif choice == 9:
    from upload.squsingfunc import *
elif choice == 10:
   from upload.sumofdigit import *
elif choice == 11:
   from upload.tictoegame import *
elif choice == 12:
   from upload.upperlowercase import *
elif choice == 13:
    from upload.welcomename import *

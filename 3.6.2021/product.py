items=[]
p=input("Enter product do u wanna buy:")
items.append(101)
items.append("nutella")
items.append(500)
items.append(5)
a=items[0]
b=items[1]
c=items[2]
d=items[3]
if p == b:
     print("ProducIid=",a)
     print("ProductPrice=",c)
     s=int(input("Enter the quantity:"))
     if s > d:
       print("This product is out of stock currently")
     else:
       z = s * c
       print("Total amount=",z)
else:
  print("Invalid product")
  



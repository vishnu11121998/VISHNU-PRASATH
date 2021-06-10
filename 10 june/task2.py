x=input("Enter name:")
y=x.title()
z=y.split()
a=""
for i in z:
 a=a+i[:-1]+i[-1].upper()+" "
print("Modified name:",a[:-1])

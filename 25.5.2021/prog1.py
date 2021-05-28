n=[] 
even=0 
odd=0 
num=int(input("Enter size:"))
for i in range(1,num+1):
    val=int(input("The elements are:" ))
    n.append(val)
for j in range(num):
    if(n[j]%2==0):
        even=even+n[j]
    else:
        odd=odd+n[j]
        a=even-odd
print(even)
print(odd)
print(a)
x=input("Enter the name:")
b=len(x)
for i in range(b):
    for j in range(b-i-1):
        print(" ",end="")
    for k in range(i+1):
        print(x[k],end="")
    print()
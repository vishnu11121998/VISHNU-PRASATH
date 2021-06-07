a=input("Enter the name:")
b=len(a)
for i in range(b):
    for j in range(i+1):
        print(a[j],end="")
    print()

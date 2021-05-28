n=[]
size=int(input("Enter size:"))
for i in range(size):
  x=int(input("Enter elements:"))
  n.append(x)
n.sort()
print(n[-1]+n[2])
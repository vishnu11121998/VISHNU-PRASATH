n=int(input())
sum=0
temp = n
while(n!=0):
   i=1
   fact=1
   n = n % 10
   while(i<=n):
      fact=fact*i
      i=i+1
      sum = sum+fact
      n=n//10
if(sum == fact):
   print("Strong number")
else:
   print("Not a strong number")
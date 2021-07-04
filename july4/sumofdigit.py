num = int(input('Enter the number'))
sum = 0
count = 0
countt = 0
number = num
while num != 0:
    num = num//10
    count += 1
while number!=0:
    n = number%10
    print(n, end="")
    if count != countt:
        print(end="+")
    sum = sum + n
    number = number//10
    countt += 1
    
print("=", int(sum))

import random
tothead = 0
tottail = 0
count = 0
while count < 10:
    coin = random.randint(1, 2)
    if coin == 1:
        print("Heads")
        tothead += 1
        count += 1
    elif coin == 2:
        print("Tails")
        tottail += 1
        count += 1
print("\nThe coin flipped heads", tothead, "times ")
print("\nThe coin flipped tails", tottail, "times ")

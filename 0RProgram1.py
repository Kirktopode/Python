import random

total = 0.0
for i in range(10000):
    count = 1
    while True:
        count += 1
        if random.randint(1,2)==1:
            break
    total += count
print total/10000, "is the average number of flips to get both heads and tails."

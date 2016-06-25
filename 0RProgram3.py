num = input("Enter a positive integer: ")
for i in range(num/2):
    if num%(i+1) == 0:
        print (i+1), "is a divisor of", num

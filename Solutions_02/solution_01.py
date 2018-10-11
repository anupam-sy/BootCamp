num = 153
total = 0

while(num != 0):
    rem = num % 10
    total = total + (rem*rem*rem)
    num = num // 10

if(num == total):
    print("Armstrong number.")
else:
    print("Not an armstrong number.")

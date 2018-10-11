num = 253
total = 0

while(num != 0):
    rem = num % 10
    total = total + rem
    num = num // 10

print("Sum of number's digit:", total)

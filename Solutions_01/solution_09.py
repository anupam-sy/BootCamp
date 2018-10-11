num = 50
flag = True

for i in range(2, num-1):
    if(num % i == 0):
        flag = False
        break

if(flag == True):
    print("Prime number.")
if(flag == False):
    print("Not a prime number.")    

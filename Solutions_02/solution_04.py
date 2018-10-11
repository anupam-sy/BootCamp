mystr = "abcdcba"

start = 0
last = len(mystr)-1
flag = False

while(start <= last):
    if(mystr[start] != mystr[last]):
        flag = True
        break
    start = start + 1
    last = last - 1

if(flag == True):
    print("Not a palindrome.")
if(flag == False):
    print("Palindrome.")


mystring = "Anupam"

def lengthChecker(mystring):
    count = 0
    for char in mystring:
        count = count + 1

    return count

length = lengthChecker(mystring)
print("Length is:", length)

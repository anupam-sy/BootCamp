mystr = "Anupam"
newstr = ""

# Iterating the loop in backward direction.
# for char in mystr[::-1]:
for char in reversed(mystr):
    newstr = newstr + char

print(newstr)

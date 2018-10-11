"""
Pattern:

*
**
***
****
*****

"""

n = int(input("Enter the number of lines:"))

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()

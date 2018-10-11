"""
Pattern:

*****
 ***
  *

"""

n = int(input("Enter the number of lines:"))

for i in range(1, n+1):
    for j in range(i-1):
        print(" ", end="")
    for k in range((2*n + 1) - (2*i)):
        print("*", end="")
    print()

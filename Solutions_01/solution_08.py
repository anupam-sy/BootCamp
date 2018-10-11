"""
Pattern:

  *
 ***
*****
 ***
  *

"""

n = int(input("Enter the number of lines:"))

for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i - 1):
        print("*", end="")
    print()

n = n - 1
for p in range(1, n+1):
    for q in range(p):
        print(" ", end="")
    for r in range((2*n + 1) - (2*p)):
        print("*", end="")
    print()

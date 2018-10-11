numList = [1,2,3,4,5,6,7,8]
evenNumList = []
oddNumList = []

for item in numList:
    if(item % 2 == 0):
        evenNumList.append(item)
    if(item % 2 != 0):
        oddNumList.append(item)

print(evenNumList)
print(oddNumList)

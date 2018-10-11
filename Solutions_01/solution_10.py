name = "Anupam Singh Yadav"
charDict = {}

for char in name:
    if(char in charDict):
        charDict[char] += 1
    if(char not in charDict):
        charDict[char] = 1

print(charDict)

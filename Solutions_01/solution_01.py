firstString = "Welcome to sanfoundry's"
secondString = "Welcome"
strJoiner = " "

tempList = firstString.split(" ")

for item in tempList:
    if(item == secondString):
        tempList.remove(item)

newstr = strJoiner.join(tempList)
print(newstr)

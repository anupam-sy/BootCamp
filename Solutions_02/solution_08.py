name = "Anupam Singh Yadav"

def reverse(word):
    
    revStr = ""
    for element in word:
        revStr = element + revStr

    return revStr

def wordSpliter(name):
    updatedStr = ""
    newStr = ""
    wordList = []
    for element in name:
        if(element != " "):
            newStr = newStr + element
        else:
            wordList.append(newStr)
            newStr = ""
    if(newStr):
        wordList.append(newStr)

    for word in wordList:
        res = reverse(word)
        updatedStr = updatedStr + " " + res

    print(updatedStr.strip())

if __name__ == "__main__":
    wordSpliter(name)

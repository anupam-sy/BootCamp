name = "Anupam Singh Yadav"

def wordSpliter(name):
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

    print(wordList)

if __name__ == "__main__":
    wordSpliter(name)

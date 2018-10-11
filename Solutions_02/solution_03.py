str1 = "Anupam"
str2 = "Anurag"

if(len(str1) != len(str2)):
    print("Strings are not matched.")
else:
    for pos in range(0, len(str1)):
        if(str1[pos] == str2[pos]):
            pass
        else:
            print("Strings are mismatched at position {}".format(pos))
            break

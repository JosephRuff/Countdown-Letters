from collections import Counter

while (True):
    print("Please enter a string: ")
    letters = Counter(input())

    wordList = []

    with open("ukenglish.txt", encoding="Latin-1") as f:
        #Content_list is the list that contains the read lines.     
        for line in f:
            line = line.rstrip("\n")
            valid = True
            
            lineCount = Counter(line)
            for x in lineCount:
                if (x in letters):
                    if (letters[x] >= lineCount[x]):
                        pass
                    else:
                        valid = False
                else:
                    valid = False
            if (valid):
                wordList.append(line)
                
                #print(lineCount)
                #print(letters)
    #print(wordList)

    for i in range (0, len(wordList) - 1):
        for j in range (0, len(wordList) - i - 1):
            #print (wordList[j] + " " + wordList[j + 1])
            if (len(wordList[j]) < len(wordList[j + 1])):
                temp = wordList[j]
                wordList[j] = wordList[j + 1]
                wordList[j + 1] = temp
            
    #print(wordList)

    for word in wordList:
        print (str(len(word)) + ": " + word)

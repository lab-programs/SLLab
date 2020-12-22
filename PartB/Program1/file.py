# Open the file
myFile = open("sample.txt", "r")

listOfLines = []
for i in myFile:
    listOfLines.append(i)

listOfWords = []
for i in listOfLines:
    words = i.split(' ')
    for j in words:
        listOfWords.append(j)

wordDict = dict()

for i in listOfWords:
    if i in wordDict.keys():
        wordDict[i] += 1

    else:
        wordDict[i] = 1

print(wordDict)
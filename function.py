def countWordsFromFile():
    fileName =  input("Enter the file name:- ")

    numberOfWords = 0

    file = open(fileName, 'r')
    for line in file:
        words = line.split()
        numberOfWords=numberOfWords+len(words)

    print("The number of words in this file are: ")
    print(numberOfWords)


countWordsFromFile()

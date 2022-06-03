def countWordsFromFile():
    FileName=input("Enter the File Name:")
    WordCount=0

    File = open(FileName, 'r')
    for i in File:
        Words = i.split()
        WordCount = WordCount+len(Words)

    print("Number of Words in File:",WordCount)

countWordsFromFile()

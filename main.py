with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    countOfWords = len(file_contents.split())
    print(countOfWords)
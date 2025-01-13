# print ("hello world")

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    amount_of_words = len(file_contents.split())
    print (amount_of_words)
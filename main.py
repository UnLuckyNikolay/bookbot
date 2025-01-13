# print ("hello world")

file_path = "books/frankenstein.txt"
with open(file_path) as f:
    file_contents = f.read().lower()
    amount_of_words = len(file_contents.split())
#    print (amount_of_words)
#    sorted_file_contents = re.sub('\W+', '', file_contents)
    amount_of_characters = {}
    for character in file_contents:
        if character in 'abcdefghijklmnopqrstuvwxyz':
            if character not in amount_of_characters:
                amount_of_characters[character] = 1
            else:
                amount_of_characters[character] += 1
#            if character == 'a' and amount_of_characters['a'] % 1000 == 0:
#                print(f'amount of a is {amount_of_characters['a']}')
    
    print(f"--- Report of {file_path} ---")
    print(f"Amount of words: {amount_of_words}")
    print()
    for word in sorted(amount_of_characters, key=amount_of_characters.get, reverse=True):
        print(f"'{word}' - {amount_of_characters[word]}")
    print("--- End of the report ---")
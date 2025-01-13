def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read().lower()
    amount_words = count_words(file_contents)
    amount_characters = count_characters_dict(file_contents)
   
    print(f"--- Report of {file_path} ---")
    print()
    print(f"Amount of words: {amount_words}")
    print()
    for word in sorted(amount_characters, key=amount_characters.get, reverse=True):
        print(f"'{word}' appeared {amount_characters[word]} times")
    print()
    print("--- End of the report ---")

def count_words(text):
    amount = len(text.split())
    return amount

def count_characters_dict(text):
    amount = {}
    for character in text:
        if character in 'abcdefghijklmnopqrstuvwxyz':
            if character not in amount:
                amount[character] = 1
            else:
                amount[character] += 1
    return amount

main()

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    characters = count_characters(book_text)

def get_book_text(book):
    with open(book) as f:
        book_contents = f.read()
        return book_contents

def count_words(book):
    word_count = len(book.split())
    words = book.split()
    return word_count, words

def count_characters(words):
    characters = {}
    for character in words:
        lowered_string = character.lower()
        if lowered_string not in characters:
            characters[lowered_string] = 0
        else: 
            characters[lowered_string] += 1
    print(characters)

main()
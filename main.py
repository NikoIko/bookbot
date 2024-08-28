def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    characters = count_characters(book_text)
    sorted_characters = sort_characters(characters)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for sorted_character in sorted_characters:
        print(f"The '{sorted_character["name"]}' was found {sorted_character["num"]} times")
    print(f"--- End report ---")


def get_book_text(book):
    with open(book) as f:
        book_contents = f.read()
        return book_contents

def count_words(book):
    word_count = len(book.split())
    return word_count

def count_characters(words):
    characters = {}
    for character in words:
        lowered_string = character.lower()
        if lowered_string not in characters:
            if lowered_string.isalpha():
                characters[lowered_string] = 1
        else: 
            characters[lowered_string] += 1
    return characters

def sort_characters(dict):
    char_list = []
    for character, count in dict.items():
        char_dict = {
            "name": character,
            "num": count,
        }
        char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def sort_on(dict):
    return dict["num"]

main()
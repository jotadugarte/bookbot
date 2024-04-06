def main():
    book_path = "books/frankenstein.txt"
    text = book_text(book_path)
    words_counted = count_words_book(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"There is {words_counted} in the document")
    character_list = count_character_appears(text)
    for item in character_list:
        print(f"The '{item["character"]}' character was found {item["count"]} times")
    print("--- End report ---")
  
def book_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_words_book(text):
    words_counted = text.split()
    words_counted = len(words_counted)
    return words_counted

def count_character_appears(text):
    character_list = {}
    for character in text.lower():
        if character.isalpha():
            if character in character_list:
                character_list[character] += 1
            else:
                character_list[character] = 1
    character_list = order_character_list(character_list)
    return character_list

def order(d):
    return d["count"]

def order_character_list(character_list):
    sorted_list = []
    for character in character_list:
        sorted_list.append({"character": character, "count": character_list[character]})
    sorted_list.sort(reverse = True, key=order)
    return sorted_list

main()
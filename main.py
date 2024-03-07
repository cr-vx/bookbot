def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word_count = count_words(text)
    letter_count = count_letters(text)
    print_data(word_count, letter_count)
   

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    characters_dict = {}
    lowered_string = text.lower()
    for char in lowered_string:
        if char not in characters_dict:
            characters_dict[char] = 1
        else:
            characters_dict[char] += 1
    return characters_dict 

def print_data(word_count, letter_count):
    print("\n=====| BOOK DATA REPORT: |=====")
    print(f"Amount of words in the book: {word_count}\n")

    lst = [{'char': key, 'count': value} for key, value in letter_count.items()]
    lst.sort(reverse=True, key=sort_on)

    for item in lst:
        if item['char'].isalpha():
            print(f"Character: {item['char']} was found {item['count']} times.")
    print("\n====| END OF REPORT |=====")

def sort_on(dict):
    return dict["count"]

main()
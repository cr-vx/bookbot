def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(f"word count: {count_words(text)}")

    print(f"chars count: {count_letter(text)}")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letter(text):
    characters_dict = {}
    lowered_string = text.lower()
    for char in lowered_string:
        if char not in characters_dict:
            characters_dict[char] = 1
        else:
            characters_dict[char] += 1
    return characters_dict 

main()
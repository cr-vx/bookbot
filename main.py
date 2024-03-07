import argparse

def main():
    parser = argparse.ArgumentParser(description="Pass in a path to a text file.\n Text is printed to console after info by default.")
    parser.add_argument("--file_path", type=str, help="Path to the text file.")
    parser.add_argument(
    "--print_text",
    type=str,
    help="Print text after info: (yes, no)",
    default="yes",
)
    args = parser.parse_args()
    path_to_txt = args.file_path
    print("path:", args.file_path)

    text = get_text(path_to_txt)
    word_count = count_words(text)
    letter_count = count_letters(text)
    print_data(word_count, letter_count)
    ask_for_print(args, text)

def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def ask_for_print(args, text):
    if args.print_text.lower() == "yes":
        print(text)
    elif args.print_text.lower() == "no":
        print("No print...")
    else:
        print("Invalid input for print permission. Please enter 'yes' or 'no'.")

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
    print("\n=====| TEXT DATA REPORT: |=====")
    print(f"Amount of words in the text: {word_count}\n")

    lst = [{"char": key, "count": value} for key, value in letter_count.items()]
    lst.sort(reverse=True, key=sort_on)

    for item in lst:
        if item['char'].isalpha():
            print(f"Character: {item["char"]} was found {item["count"]} times.")

    print("\n====| END OF REPORT |=====")

def sort_on(dict):
    return dict["count"]

main()
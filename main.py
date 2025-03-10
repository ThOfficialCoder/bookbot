import sys
from stats import get_word_count, num_of_chars, print_info

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        text = f.read()

    num_words = get_word_count(text)

    char_count = num_of_chars()

    sorted_counts = print_info(char_count)

    print(f"{get_word_count(num_words)} words found in the document")
    print(f"{num_of_chars()}")

    for item in sorted_counts:
        print(f"{item}")

    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

main()
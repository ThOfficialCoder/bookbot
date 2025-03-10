import sys

def get_word_count(text):
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        book_text = f.read()

    words_split = book_text.split()

    return len(words_split)


def num_of_chars():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    word_list = {}
    with open(file_path, "r") as f:
        word = f.read()

    num_of_times = word.lower()

    for item in num_of_times:
        if item in word_list:
            word_list[item] += 1
        else:
            word_list[item] = 1

    return word_list


def print_info(char_count):
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    with open(file_path, "r") as f:
        text = f.read()

    new_list = []

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(text)} total words")
    print("--------- Character Count -------")

    for word, count in char_count.items():
        if word.isalpha():
            new_list.append(f"{word}: {count}")

    new_list.sort(key=lambda x: int(x.split(": ")[1]), reverse=True)


    return new_list

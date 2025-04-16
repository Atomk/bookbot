import sys
from stats import count_words, character_frequency, process_characters_dict

def get_book_text(filepath) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def print_character_frequency(book_text, max_lines=0):
    assert(max_lines >= 0)
    freq_dict = character_frequency(book_text)
    sorted_freqs = process_characters_dict(freq_dict)
    count_lines = 0

    for entry in sorted_freqs:
        if not entry["character"].isalpha():
            continue
        print(f"{entry["character"]}: {entry["count"]}")

        count_lines += 1
        if max_lines > 0 and count_lines == max_lines:
            skipped = len(freq_dict) - count_lines
            if skipped > 0:
                print(f"...{skipped} more")
            return

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    try:
        book_text = get_book_text(book_path)
    except FileNotFoundError as e:
        print(e)
        print("note: path has to be absolute, or relative to `main.py`")
        return

    num_words = count_words(book_text)
    freq_dict = character_frequency(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("------ Character Frequency ------")
    print_character_frequency(book_text, 10)

    sorted_freqs = process_characters_dict(freq_dict)
    for entry in sorted_freqs:
        if entry["character"].isalpha():
            print(f"{entry["character"]}: {entry["count"]}")

    print("============= END ===============")

main()
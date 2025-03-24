from stats import count_words, character_frequency, process_characters_dict

def get_book_text(filepath) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    freq_dict = character_frequency(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    sorted_freqs = process_characters_dict(freq_dict)
    for entry in sorted_freqs:
        if entry["character"].isalpha():
            print(f"{entry["character"]}: {entry["count"]}")

    print("============= END ===============")

main()
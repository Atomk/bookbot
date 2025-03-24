from stats import count_words, character_frequency

def get_book_text(filepath) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    frankenstein = get_book_text("./books/frankenstein.txt")
    num_words = count_words(frankenstein)
    print(f"{num_words} words found in the document")

    freq_dict = character_frequency(frankenstein)
    print(freq_dict)

main()
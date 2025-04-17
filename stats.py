def count_words(text: str) -> int:
    return len(text.split())


def character_frequency(text: str) -> dict[str, int]:
    chars_dict = {}

    for char in text:
        char = char.lower()
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1

    return chars_dict

def sort_on(dict):
    return dict["count"]

def process_characters_dict(input) -> list[dict]:
    sorted_list = []
    for charecter in input:
        sorted_list.append( { "character": charecter, "count": input[charecter] } )

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def word_frequency_sorted(text: str, case_sensitive=False) -> list[dict]:
    words_dict = {}
    words = text.split() if case_sensitive else text.lower().split()

    for word in words:
        if word not in words_dict:
            words_dict[word] = 0
        words_dict[word] += 1

    list_of_dicts = [ { "word": key, "count": val } for key, val in words_dict.items() ]
    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts

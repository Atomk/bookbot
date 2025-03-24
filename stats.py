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

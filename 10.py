def count_chars(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count


print(count_chars('sffss'))

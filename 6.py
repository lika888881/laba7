from string import punctuation


def strip_punctuation_ru(data):
    return ''.join([char for char in data
                    if char not in punctuation])


print(strip_punctuation_ru(input()))

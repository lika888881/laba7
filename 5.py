def strip_punctuation_ru(data):
    pass


def test_strip_punctuation_ru():
    data = ['abs, pop', 'abc']
    results = ['abs pop', 'abc']

    flag = False

    for item, result in zip(data, results):
        if strip_punctuation_ru(item) != result:
            flag = True

    if not flag:
        print('YES')
    else:
        print('NO')

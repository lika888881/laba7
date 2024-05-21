def is_palindrome(data):
    pass


def test_is_palindrome():
    data = ['aba', '123', 'abcd', 'bb']
    results = [True, False, False, True]

    flag = False

    for item, result in zip(data, results):
        if is_palindrome(item) != result:
            flag = True

    if not flag:
        print('YES')
    else:
        print('NO')

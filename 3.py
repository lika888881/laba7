def is_correct_mobile_phone_ru(number):
    pass


def test_test_is_correct_mobile_phone_ru():
    data = ['+79871073085', '8913', '777', '+7(987)1073085', '+7 987 107 30 85']
    results = [True, False, False, True, True]

    flag = False

    for item, result in zip(data, results):
        if is_correct_mobile_phone_ru(item) != result:
            flag = True

    if not flag:
        print('YES')
    else:
        print('NO')


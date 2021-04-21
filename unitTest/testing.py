from is_greater import is_greater

def publish_result(test):
    def innerfunc():
        value = test()
        if value[0] == value[1]:
            result = "PASS"
        else:
            result = "FAIL"
        print(f"{test.__name__}: {result}")
    return innerfunc


@publish_result
def test_true_when_greater():
    testresult = [is_greater(5, 4), True]
    return testresult


@publish_result
def test_false_when_smaller():
    testresult = [is_greater(4, 5), False]
    return testresult


@publish_result
def test_false_when_equal():
    testresult = [is_greater(5, 5), False]
    return testresult


if __name__ == "__main__":
    test_true_when_greater()
    test_false_when_smaller()
    test_false_when_equal()
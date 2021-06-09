import Task3


def test_isPhoneNumber():
    tests = [("98882 47474", True), ("88882 47474", True), ("78882 47474", True), ("9888247474", False),
             ("58882 47474", False), ("2888247474", False)]
    for number, result in tests:
        assert Task3.isMobileNumber(number) == result


def test_isTelemarketerNumber():
    tests = [("1408247474", True), ("1208247474", False),
             ("7888247474", False)]
    for number, result in tests:
        assert Task3.isTelemarketerNumber(number) == result


def test_isFixedNumber():
    tests = [("(080)1408247474", True), ("(380)1408247474", False), ("(026362)1408247474",
                                                                     True), ("1208(080)247474", False), ("9208247474", False), ("(022)7888247474", True)]
    for number, result in tests:
        assert Task3.isFixedNumber(number) == result


def test_isFromBangalore():
    tests = [("(080)1408247474", True), ("1208(080)247474", False),
             ("(022)7888247474", False)]
    for number, result in tests:
        assert Task3.isFromBangalore(number) == result

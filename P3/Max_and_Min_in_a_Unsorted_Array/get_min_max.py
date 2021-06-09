import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
    ints(list): list of integers containing one or more integers
    """
    max_number = ints[0]
    min_number = ints[0]

    for number in ints[1:]:

        if(number > max_number):
            max_number = number

        if(number < min_number):
            min_number = number

    return min_number, max_number


# Example Test Case of Ten Integers



def test_cases(input_case):

    random.shuffle(input_case)

    print("Pass" if (max(input_case), min(input_case)
                     == get_min_max(input_case)) else "Fail")


test_cases([i for i in range(0, 10)]) # a list containing 0 - 9

test_cases([-i for i in range(0, 10)]) # a list containing 0 - -9

test_cases([0]) # 0

test_cases([i for i in range(-99, 99)]) # a list containing -99  99

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    frequency = {}
    for value in input_list:                # O(n)
        frequency[value] = frequency.get(value, 0) + 1

    left = False

    result = [0, 0]
    for key in range(9,-1,-1):
        frequency_value = frequency.get(key)
        if frequency_value == None:
            continue

        nums = [key] * frequency_value
        for n in nums:
            if(left):
                result[0] *= 10
                result[0] += n
            else:
                result[1] *= 10
                result[1] += n

            left = not left

    return result


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[1, 2, 2, 2, 3, 4, 5], [5422, 321]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1, 0, 1, 0], [10, 10]])
test_function([[4, 6, 2, 5, 3, 9, 8, 1, 0], [96420, 8531]])
test_function([[1, 0], [1, 0]])
test_function([[0, 0], [0, 0]])
test_function([[2, 2], [2, 2]])

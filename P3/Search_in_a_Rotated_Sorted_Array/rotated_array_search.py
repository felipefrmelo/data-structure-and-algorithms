import random

def checksIfValueIsBetweenaRange(
    target, smaller, bigger): return target >= smaller and target <= bigger


def rangeIsSorted(
    start_element, end_element): return end_element - start_element >= 0


def checkIfElementIsOnTheLeftSide(target, start_element, mid_element, end_element):

    if rangeIsSorted(start_element, mid_element):
        return checksIfValueIsBetweenaRange(target, start_element, mid_element)

    return not checksIfValueIsBetweenaRange(target, mid_element, end_element)


def rotated_array_search(input_list, target):
    """
    Find the index by searching in a rotated sorted array

    Args:
        input_list(array), number(int): Input array to search and the target
    Returns:
        int: Index or -1
    """
    start_index = 0
    end_index = len(input_list) - 1

    while start_index <= end_index:

        mid_index = (start_index + end_index)//2

        mid_element = input_list[mid_index]
        start_element = input_list[start_index]
        end_element = input_list[end_index]

        if(mid_element == target):
            return mid_index

        if checkIfElementIsOnTheLeftSide(target, start_element, mid_element, end_element):
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1

    return - 1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        raise Exception("Fail")


test_function([[4, 5, 6, 7, 0, 1, 2], 1])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 3])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])


# Edge cases
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 0])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], 10])
test_function([[1, 2, 3, 4, 5, 6, 7, 8], 5])
test_function([[2, 3, 4, 5, 6, 7, 8, 1], 5])
test_function([[8, 9, 1, 2, 3, 4, 5, 6, 7], 9])

# random test
num_test = 100
counter = 0
while counter < num_test:
    counter += 1
    input_list = list({random.randint(0, 100)
                       for _ in range(random.randint(1, 100))})
    input_list.sort()
    pivot = random.randrange(0, len(input_list))
    rotate = input_list[pivot:] + input_list[:pivot]
    random_target = random.randrange(0, len(input_list))

    test_function([rotate, random_target])

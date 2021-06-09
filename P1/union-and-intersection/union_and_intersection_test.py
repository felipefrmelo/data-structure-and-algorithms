from union_and_intersection import intersection, union, LinkedList


def make_linked_list(elements):
    linked_list = LinkedList()
    for i in elements:
        linked_list.append(i)
    return linked_list


def helper(element_1, element_2, expected_union, expected_intersection):

    linked_list_1 = make_linked_list(element_1)
    linked_list_2 = make_linked_list(element_2)

    result_union = union(linked_list_1, linked_list_2)
    assert len(expected_union) == result_union.size()
    for expected in expected_union:
        assert str(expected) in str(union(linked_list_1, linked_list_2))

    result_intersection = intersection(linked_list_1, linked_list_2)
    assert len(expected_intersection) == result_intersection.size()
    for expected in expected_intersection:
        assert str(expected) in str(intersection(linked_list_1, linked_list_2))


def test_union_and_intersection():
    helper([1, 2, 3, 4, 5, 6], [6, 7, 8], [
        1, 2, 3, 4, 5, 6, 7, 8, ], [6])

    # one list is empty
    helper([], [1, 2, 3], [1, 2, 3], [])

    # both lists are empty
    helper([], [], [], [])

    # list equals
    helper([1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3])

    # list without equal elements
    helper([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6], [])

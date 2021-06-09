

from prims_algorithm import get_minimum_cost_of_connecting


def test_prims_algorithm_with_2_islands():
    num_islands = 2
    bridge_config = [[1, 2, 1]]

    cost = get_minimum_cost_of_connecting(num_islands, bridge_config)

    assert cost == 1

def test_prims_algorithm_with_3_islands():
    num_islands = 5
    bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
    solution = 13

    test_case = [num_islands, bridge_config, solution]
    helper(test_case)

    num_islands = 5
    bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
    solution = 31
    test_case = [num_islands, bridge_config, solution]
    helper(test_case)
    
def helper(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)

    assert output == solution

from huffman_coding import frequency_of_each_character, build_a_priority_queue, Node, huffman_decoding, huffman_encoding, merge_nodes, pop_out_two_nodes


def test_frequency_of_each_character():

    message = "AAAAAAABBBCCCCCCCDDEEEEEE"

    assert {'A': 7, 'B': 3,  'D': 2, 'C': 7,
            'E': 6} == frequency_of_each_character(message)

    message = "The bird is the word"

    assert {' ': 4, 'e': 2, 'h': 2, 'i': 2, 'o': 1, 'r': 2, 's': 1,
            't': 1, 'w': 1, 'T': 1, 'b': 1, 'd': 2} == frequency_of_each_character(message)


def test_build_a_priority_queue():

    priorityQueue = build_a_priority_queue(
        {'A': 7, 'B': 3,  'D': 2, 'C': 7, 'E': 6})

    assert priorityQueue.dequeue() == Node(2, "D")
    assert priorityQueue.dequeue() == Node(3, "B")
    assert priorityQueue.dequeue() == Node(6, "E")
    assert priorityQueue.dequeue() == Node(7, "A")
    assert priorityQueue.dequeue() == Node(7, "C")

    priorityQueue = build_a_priority_queue({' ': 4, 'e': 2, 'h': 2, 'i': 2, 'o': 1, 'r': 2, 's': 1,
                                            't': 1, 'w': 1, 'T': 1, 'b': 1, 'd': 2})

    assert priorityQueue.dequeue() == Node(1, "o")
    assert priorityQueue.dequeue() == Node(1, "t")
    assert priorityQueue.dequeue() == Node(1, "b")
    assert priorityQueue.dequeue() == Node(1, "w")


def test_pop_out_two_nodes_from_priotity_queue():
    priorityQueue = build_a_priority_queue(
        {'A': 7, 'B': 3,  'D': 2, 'C': 7, 'E': 6})

    left, right = pop_out_two_nodes(priorityQueue)

    assert left == Node(2, "D")
    assert right == Node(3, "B")


def test_merge_nodes():
    left, right = Node(2, "D"), Node(3, "B")

    newNode = merge_nodes(left, right)
    assert newNode.left_child == Node(2, "D")
    assert newNode.right_child == Node(3, "B")
    assert newNode.frequency == 5


def test_huffman_encoding():
    message = "AAAAAAABBBCCCCCCCDDEEEEEE"

    encoded, tree = huffman_encoding(message)
    assert encoded == "1010101010101000100100111111111111111000000010101010101"

    assert huffman_decoding(encoded, tree) == message

    message = "AAAA"

    encoded, tree = huffman_encoding(message)
    assert encoded == "0000"

    assert huffman_decoding(encoded, tree) == message


def test_huffman_encoding_when_string_is_empty():

    encoded, tree = huffman_encoding("")
    assert encoded == None

    encoded, tree = huffman_encoding(None)
    assert encoded == None

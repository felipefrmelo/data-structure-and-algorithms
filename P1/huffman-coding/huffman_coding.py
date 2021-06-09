from priority_queue import PriorityQueue

import sys


class Node:

    def __init__(self, frequency=None, character=None):
        self.frequency = frequency
        self.character = character
        self.left_child: Node = None
        self.right_child: Node = None

    @property
    def has_left_child(self):
        return self.left_child != None

    @property
    def has_right_child(self):
        return self.right_child != None

    @property
    def is_leaf(self):
        has_child = self.has_left_child or self.has_right_child
        return not has_child

    def __lt__(self, other):
        if (self.frequency == other.frequency):
            return self.character and other.character and self.character < other.character

        return self.frequency < other.frequency

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.frequency == other.frequency and self.character == other.character

    def __gt__(self, other):
        return other.frequency < self.frequency

    def __repr__(self):
        return f"Node(freq={self.frequency}, char={self.character})"


def frequency_of_each_character(string):
    result = {}
    for bit in string:
        result[bit] = result.get(bit, 0) + 1
    return result


def build_a_priority_queue(data: dict) -> PriorityQueue:
    priorityQueue = PriorityQueue()
    for character, frequency in data.items():
        priorityQueue.enqueue(Node(frequency, character))

    return priorityQueue


def pop_out_two_nodes(queue: PriorityQueue):
    left = queue.dequeue()
    right = queue.dequeue()
    return left, right


def merge_nodes(left: Node, right: Node):
    newNode = Node(left.frequency + right.frequency)
    newNode.left_child = left
    newNode.right_child = right
    return newNode


class HuffmanTree:

    def __init__(self, root: Node) -> None:
        self.root = root
        self.generate_huffman_code()

    def generate_huffman_code(self):
        if(self.root.is_leaf):
            self.encoding = {self.root.character: "0"}
            return

        self.encoding = {}

        def traverse(node, code=""):
            if node:
                traverse(node.left_child, code + "0")

                traverse(node.right_child, code + "1")

                char = node.character
                if(char != None):
                    self.encoding[char] = code
        traverse(self.root)

    def encode(self, data):
        return "".join([self.encoding[char] for char in data])

    def decode(self, data):
        decoded = ""
        node = self.root

        if(node.is_leaf):
            return node.character * len(data)

        for bit in data:
            if(bit == "0"):
                node = node.left_child
            else:
                node = node.right_child

            if(node.is_leaf):
                decoded += node.character
                node = self.root

        return decoded


def huffman_encoding(data):
    # O(n)

    if(not data):
        return None, None
    frequency = frequency_of_each_character(data)

    #O(n * log(n))
    queue = build_a_priority_queue(frequency)

    #O(n * log(n))
    while queue.size > 1:
        #O(2 * log(n))
        left, rigth = pop_out_two_nodes(queue)
        # O(1)
        newNode = merge_nodes(left, rigth)
        # O(log(n))
        queue.enqueue(newNode)

    # O(n)
    tree = HuffmanTree(queue.dequeue())
    # O(n)
    return tree.encode(data), tree


def huffman_decoding(data, tree):
    # O(n)
    return tree.decode(data)


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

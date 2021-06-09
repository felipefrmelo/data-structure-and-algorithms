import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        def encode(x): return str(x).encode("utf-8")

        sha.update(encode(self.data) + encode(self.timestamp) +
                   encode(self.previous_hash))

        return sha.hexdigest()

    def __str__(self):
        return f'\nTimestamp: {self.timestamp}\nData: {self.data}\nPrevious Hash: {self.previous_hash}\nHash: {self.hash}\n'


class Node:
    def __init__(self, data, previous_hash=""):
        self.block = Block(datetime.utcnow().isoformat(), data, previous_hash)
        self.next = None


class BlockChain:

    def __init__(self) -> None:
        self.genesis_block: Node = None
        self.tail: Node = None
        self.size = 0

    def add_block(self, data):

        if(not data):
            raise ValueError("Block cannot be null")
        if self.genesis_block:
            newNode = Node(data, self.tail.block.hash)
            self.tail.next = newNode
            self.tail = newNode

        else:
            newNode = Node(data, None)
            self.genesis_block = newNode
            self.tail = newNode

        self.size += 1

    def __str__(self):
        if self.genesis_block == None:
            return "is empty"
        current_node = self.genesis_block
        output = ""
        while current_node:
            output += str(current_node.block)
            current_node = current_node.next
        return output


block_chain = BlockChain()
block_chain.add_block("Some Information")
block_chain.add_block("Foo")
block_chain.add_block("Bar")


current_block = block_chain.genesis_block
print(block_chain)

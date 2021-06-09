class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        self.children[char] = TrieNode()

    def charIsInChildren(self, char):
        return char in self.children


    def __repr__(self):
        return f"{self.children}"

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        suffixes = []

        if(self.is_word and suffix):
            suffixes.append(suffix)

        for char, children in self.children.items():
            suffixes += children.suffixes(suffix + char)

        return suffixes


class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        current = self.root

        for char in word:
            if(not current.charIsInChildren(char)):
                current.insert(char)
            current = current.children[char]

        current.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix

        current = self.root

        for char in prefix:
            if(not current.charIsInChildren(char)):
                return None

            current = current.children[char]

        return current


def test(prefix, expected = []):
    prefix_node = MyTrie.find(prefix)
    print(f"{prefix} - {prefix_node.suffixes()}")
    if prefix_node.suffixes() == expected:
        print('pass\n')
    else:
        print("fail\n")

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    MyTrie.insert(word)


test('', wordList)

test('f', ['un', 'unction', 'actory'])
test('an', ['t', 'thology', 'tagonist', 'tonym'])

test('ant',['hology', 'agonist', 'onym'])

test('tripod', [])
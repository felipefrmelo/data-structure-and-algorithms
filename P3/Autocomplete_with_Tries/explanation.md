## Building a Trie in Python

Given a  node, the solution recursively loops through all of the node's children. Whenever a "word" node is encountered, it is added to the list of suffixes.

### Efficiency

- Time complexity  O(n):
  - insert  O(n)
  - find    O(n)
  - suffixes in worse case, we would need to visit every node in the entire trie. O(n)

- The space complexity O(n) 
  - The worst-case scenario when constructing a trie is that none of the words in the trie share a common root.



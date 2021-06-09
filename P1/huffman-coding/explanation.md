## Huffman Coding


The algorithm is utilizing a Tree, a Queue, a MinHeap, and a Hashmap. To encode the data first I counted the frequency of each charachter, then built heapafied tree where the leaf nodes were the charachters the depth of each charachter in the tree is determined by their frequency in the data.

### Time Complexity

  - encoding: `O(n * log(n))` for:

    - finding the frequency of each charachter is `O(n)` (loop once through the input)
    - To build the tree, a PriorityQueue is used to store the nodes, where insertion and removal is `O(log(n))`
    - generating the code: `O(n)` where in the the number of unique charachters in the data (the number of leafes in the tree)
    - replacing the charachters in the string (encode), takes `O(n)`

  - decoding: `O(n)`
    - where n is the length of the encoded data for building the string,

### Space Complexity:
  - `O(n*log(n))` from the tree for encoding
  - decoding `O(n)` where n is the length of the string.

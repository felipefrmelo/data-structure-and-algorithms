## Blockchain

The problem calls for a linked list. This is a singly linked list that maintains a tail pointer. New blocks are appended and the tail always points to the most recently added block.

### Time complexity

- Insertions have average and worst case `O(1)`. If there are n items in the list (blockchain) and each item takes up m amount of memory the space complexity would be O(n\*m).

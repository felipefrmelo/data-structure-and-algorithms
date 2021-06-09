## HTTPRouter using a Trie

The design follows how the problem is laid out. Three classes: a router trie node, a router trie and a router

### Efficiency

- Time Complexity:
   - insert: O(n) The insert operation saying that n = each '/', takes O(n) because there is one iteration per path part
   - find: O(n) Almost the same process, iterating through input one time, O(n)
- Space Complexity:
   - insert: path_parts occupies n but splitted, so takes O(n)
   - find: path_parts occupies n but splitted, so takes O(n)
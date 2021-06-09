## Rearrange Array Elements

since we assume that all the elements of the matrix are in the range [0, 9], we can create a dict being that the key represents the element and its value the frequency, so we interact from 9 to 0 adding digits to the numbers until the frequency is 0. then we return an array of the two numbers.

### Efficiency

- Time complexity  O(n)
- The space Complexity O(1) 
 

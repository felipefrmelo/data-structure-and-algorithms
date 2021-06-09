## Finding the square root of an integer

Suppose we know an interval [a, b] such that f (a) f (b) < 0.

- Calculate the midpoint of the range
- Evaluate f at the midpoint, that is, calculate f (m)
- Replace a or b with m in order to obtain a new range that contains the root
- We repeat until we get "a" equal to "m", or f (m) equal to zero

### Efficiency

- Time complexity  O(log(n)):
  - at each iteration we divide the initial interval in half
- The space efficiency O(1) 
  - No temporary data structures are used in order to arrive at the solution.

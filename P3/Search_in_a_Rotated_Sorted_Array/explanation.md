## Search in a Rotated Sorted Array

The algorithm is the same as for binary search, with a difference, when checking whether the target is on the left or right side, we do:
If the left side is ordered, we check if the target value is in the left half. Otherwise, we check that the target value is not in the right half.

### Efficiency

- Time complexity  O(log(n)):
  - at each iteration we divide the initial interval in half
- The space efficiency O(1) 
  - No temporary data structures are used in order to arrive at the solution.

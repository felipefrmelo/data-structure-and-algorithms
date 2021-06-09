## File recursion 

This problem use a combination of recursion and iteration over each folder, just iterate among each directory and each sub directory with a list filtering files with the extension required

### Time and Space complexity:
- Time O(n * m) -> Because per each initial folder we need to iterate among all the things inside(other variable thats m)
- Space O(n * m) -> We need an array of size m for each folder (n)
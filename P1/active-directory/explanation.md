## Active Directory

### Time complexity
n - is number of groups
m - is number of users

To find particular user needs to traverse all groups `O(n)` (in worst case) and check it's users for `O(1)`. 
`visited_groups` is `set`, so put/check operations also has `O(1)` time complexity.

### Space complexity
To avoid cycles we have to store all visited groups. In worst case it will be `O(n)`.
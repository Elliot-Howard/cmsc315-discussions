# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

# Unit 4 Discussion: Binary Search Trees

## Overview

For this assignment, I created a Binary Search Tree (BST) in Python. I used employee ID numbers as a real-world example to demonstrate how a BST organizes and searches for information.

## Implementation

I created a Node class and a BST class. I implemented recursive insertion, recursive searching, and in-order traversal.

I inserted seven employee IDs: 1050, 1025, 1075, 1010, 1035, 1060, and 1090.

Smaller values were placed in the left subtree, while larger values were placed in the right subtree. The in-order traversal displayed the values in ascending order.

## Testing and Results

I tested the following operations:

- Inserted seven employee IDs into the BST.
- Performed an in-order traversal.
- Searched for existing IDs (1050 and 1035).
- Searched for missing IDs (1000 and 1100).
- Tested searching and traversing an empty tree.
- Tested inserting a duplicate value.
- Tested a tree containing only one node.

The in-order traversal returned:

[1010, 1025, 1035, 1050, 1060, 1075, 1090]

All tests produced the expected results.

## Challenges and What I Learned

One challenge was understanding how recursion worked when inserting and searching for values. I learned that each comparison determined whether the program moved to the left or right subtree.

I also learned that insertion order affected the efficiency of a BST. A balanced BST could search in O(log n) time, while an unbalanced BST could take O(n) time in the worst case.

## Real-World Application

I used employee ID numbers to demonstrate how a company could organize employee records. A BST could help locate employee IDs efficiently without searching through every record when the tree was balanced.

## Conclusion

This assignment helped me understand recursive tree operations, BST organization, and how the structure of a tree affected search performance.
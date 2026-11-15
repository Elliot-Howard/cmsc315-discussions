# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compared linear search and binary search by implementing both algorithms in Python. I tested their functionality using small and large datasets, demonstrated edge cases, and examined their performance differences.

## Learning Objectives

- Implemented linear search.
- Implemented binary search.
- Compared search performance using different dataset sizes.
- Analyzed algorithm efficiency and time complexity.
- Applied search algorithms to a real-world scenario.

## Implementation

### Linear Search

I implemented linear search by checking each element in the list sequentially until the target value was found or the end of the list was reached. The function returned the index when the value was found and returned -1 when it was not found.

Linear search had a time complexity of O(n) because it potentially examined every element in the collection.

### Binary Search

I implemented binary search using two boundary variables to identify the current search range. The algorithm examined the middle element and eliminated half of the remaining search range during each iteration.

The function returned the target's index when found and -1 when the target was not present. Binary search had a time complexity of O(log n) because the search range was divided in half during each iteration.

The input list was required to be sorted before binary search could be performed.

## Testing and Results

### Small Dataset

I created a sorted list containing seven integers. Both algorithms successfully located an existing value and returned -1 when searching for a value that was not present.

### Large Dataset

I created a sorted dataset containing 100,000 even numbers. Both algorithms successfully located the target value. I used Python's time module and `time.perf_counter()` to measure their execution times.

The results demonstrated that binary search was more efficient for the large sorted dataset because it eliminated half of the remaining search range during each iteration.

### Edge Cases

I tested the following edge cases:

1. **Empty list:** Both algorithms returned -1 because there were no elements to search.
2. **Single-element list:** Both algorithms successfully located the target at index 0.
3. **Missing value:** Both algorithms returned -1 when the target was not present.
4. **Boundary values:** Binary search successfully located values at the first and last positions of the list.

These tests demonstrated that both implementations handled empty collections, missing values, and boundary conditions correctly.

## Real-World Application

A real-world application of these algorithms is searching for a specific contact in a digital contact list.

Linear search could be used when contacts were stored without a particular order. It would examine each contact until the correct one was found.

Binary search would be more appropriate when contacts were organized alphabetically. It could repeatedly narrow the search range, making it significantly faster when searching through a large collection.

## Performance Analysis

Linear search had a time complexity of O(n), meaning its search time increased proportionally with the number of elements.

Binary search had a time complexity of O(log n), making it more efficient for large, sorted datasets.

However, binary search required sorted data. If a collection was small or frequently changing, the time required to sort it might outweigh the benefits of faster searching. In those situations, linear search could be the more practical choice.

## Conclusion

This assignment demonstrated how linear search and binary search approached the same problem differently. I found that linear search was simpler and worked with unsorted data, while binary search provided better performance when working with sorted collections. Testing different dataset sizes and edge cases helped demonstrate the importance of selecting an appropriate algorithm based on the organization and size of the data.
"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""
import time


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Check each element from the beginning of the list.
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    # Every element may need to be checked, giving O(n) time.
    return -1




def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    left = 0
    right = len(lst) - 1

    while left <= right:
        # Find the middle position of the remaining search range.
        middle = (left + right) // 2

        if lst[middle] == target:
            return middle

        elif lst[middle] < target:
            # Eliminate the middle and everything to its left.
            left = middle + 1

        else:
            # Eliminate the middle and everything to its right.
            right = middle - 1

    # The search range is empty, so the target was not found.
    return -1



def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================

    print("\n=== SMALL DATASET TEST ===")

    # A small sorted collection of values.
    small_data = [5, 10, 15, 20, 25, 30, 35]

    # Test a value that exists in the collection.
    target = 25

    linear_result = linear_search(small_data, target)
    binary_result = binary_search(small_data, target)

    print("Small dataset:", small_data)
    print("Searching for:", target)
    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    # Test a value that does not exist.
    missing_target = 40

    print("\nSearching for missing value:", missing_target)
    print("Linear search:", linear_search(small_data, missing_target))
    print("Binary search:", binary_search(small_data, missing_target))

    # Both algorithms return -1 when the target is missing.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================

    print("\n=== LARGE DATASET TEST ===")

    # Create a sorted dataset containing 100,000 even numbers.
    large_data = list(range(0, 200000, 2))

    # Search near the end to demonstrate the difference
    # between checking elements individually and halving the search range.
    large_target = 199998

    import time

    # Measure linear search execution time.
    start_time = time.perf_counter()
    linear_result = linear_search(large_data, large_target)
    linear_time = time.perf_counter() - start_time

    # Measure binary search execution time.
    start_time = time.perf_counter()
    binary_result = binary_search(large_data, large_target)
    binary_time = time.perf_counter() - start_time

    print("Dataset size:", len(large_data))
    print("Searching for:", large_target)
    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    print(f"Linear search time: {linear_time:.8f} seconds")
    print(f"Binary search time: {binary_time:.8f} seconds")

    # Linear search may examine nearly every element.
    # Binary search eliminates half of the remaining elements
    # during every iteration, making it more efficient for
    # large, sorted datasets.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Searching an empty list.
    empty_data = []

    print("\nEdge Case 1: Empty list")
    print("Linear search:", linear_search(empty_data, 10))
    print("Binary search:", binary_search(empty_data, 10))

    # Both algorithms return -1 because no elements exist.

    # Edge case 2: Searching a single-element list.
    single_data = [50]

    print("\nEdge Case 2: Single-element list")
    print("Searching for 50:")
    print("Linear search:", linear_search(single_data, 50))
    print("Binary search:", binary_search(single_data, 50))

    # Both algorithms find the value at index 0.

    print("\nSearching for 25 in the single-element list:")
    print("Linear search:", linear_search(single_data, 25))
    print("Binary search:", binary_search(single_data, 25))

    # Both algorithms return -1 because 25 is not present.

    # Edge case 3: First and last positions.
    boundary_data = [10, 20, 30, 40, 50]

    print("\nEdge Case 3: Boundary values")
    print("First element (10):", binary_search(boundary_data, 10))
    print("Last element (50):", binary_search(boundary_data, 50))

    # Binary search correctly handles both boundaries.


if __name__ == "__main__":
    main()

"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        # Start at the root and recursively find the correct position.
        # Smaller values go left, and larger values go right.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """

        # An empty position means the value can be inserted here.
        if node is None:
            return Node(value)

        # Smaller values belong in the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values belong in the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate employee IDs are ignored.
        # Return the current node to maintain the tree structure.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """

        # A BST can eliminate an entire subtree after each comparison.
        # A linear search may need to examine every item.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        # Reaching an empty position means the value was not found.
        if node is None:
            return False

        # The requested value matches the current node.
        if value == node.value:
            return True

        # Search only the subtree where the value could exist.
        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """

        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        if node is None:
            return

        # Visit smaller values first.
        self._inorder_recursive(node.left, values)

        # Add the current node's value.
        values.append(node.value)

        # Visit larger values last.
        self._inorder_recursive(node.right, values)

        # Left, root, right produces ascending order in a BST.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    # Real-world example: organizing employees by unique ID numbers.
    employee_tree = BST()

    employee_ids = [1050, 1025, 1075, 1010, 1035, 1060, 1090]

    for employee_id in employee_ids:
        employee_tree.insert(employee_id)

    print("Employee IDs inserted:", employee_ids)
    print("Root employee ID:", employee_tree.root.value)

    # BST searching follows only one subtree at each comparison.
    # In a balanced tree, this reduces the remaining search space
    # by approximately half at each level.

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    sorted_ids = employee_tree.inorder()

    print("Sorted employee IDs:", sorted_ids)

    # In-order traversal visits the left subtree, current node,
    # and right subtree, producing values in ascending order.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    search_ids = [1050, 1035, 1000, 1100]

    for employee_id in search_ids:
        found = employee_tree.search(employee_id)

        if found:
            print(f"Employee ID {employee_id}: Found")
        else:
            print(f"Employee ID {employee_id}: Not found")

    # Existing IDs return True.
    # Missing IDs return False when the search reaches None.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Test 1: An empty tree has no values to traverse or search.
    empty_tree = BST()

    print("Empty tree traversal:", empty_tree.inorder())
    print("Search empty tree for 1050:", empty_tree.search(1050))

    # Test 2: Duplicate values are ignored.
    employee_tree.insert(1050)

    print("After inserting duplicate 1050:", employee_tree.inorder())

    # Test 3: A tree with one node still supports both operations.
    single_tree = BST()
    single_tree.insert(2000)

    print("Single-node traversal:", single_tree.inorder())
    print("Single-node search for 2000:", single_tree.search(2000))
    print("Single-node search for 3000:", single_tree.search(3000))

    # ===============================
    # ADDITIONAL TEST: INSERTION ORDER
    # ===============================

    print("\n=== INSERTION ORDER COMPARISON ===")

    # Sequential insertion creates a right-skewed tree.
    sequential_tree = BST()
    sequential_ids = [1001, 1002, 1003, 1004, 1005, 1006, 1007]

    for employee_id in sequential_ids:
        sequential_tree.insert(employee_id)

    print("Sequential insertion:", sequential_ids)
    print("In-order traversal:", sequential_tree.inorder())

    # Both trees produce sorted output, but their shapes differ.
    # A balanced BST can search in O(log n) time.
    # A skewed BST may require O(n) time in the worst case.

    print("\n=== UNIT 4 TESTS COMPLETE ===")


if __name__ == "__main__":
    main()

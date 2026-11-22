"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")
    print("Scenario: Tracking a CAP uniform inventory")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")

    # A dictionary uses hashes of keys to organize and locate entries.
    # The key identifies a uniform item and size; the value is its quantity.
    inventory = {}

    inventory["ABU blouse - medium"] = 4
    inventory["ABU blouse - large"] = 3
    inventory["ABU trousers - medium"] = 5
    inventory["Service coat - medium"] = 2
    inventory["Flight cap - small"] = 6

    print("Current uniform inventory:")
    for item, quantity in inventory.items():
        print(f"  {item}: {quantity} available")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # A dictionary uses the key's hash to help find its associated value.
    # Lookup is typically O(1) on average, though collisions can add work.
    blouse_quantity = inventory["ABU blouse - medium"]
    cap_quantity = inventory["Flight cap - small"]

    print(f"ABU blouse - medium: {blouse_quantity} available")
    print(f"Flight cap - small: {cap_quantity} available")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print(f"Inventory before update: {inventory}")

    # Assigning a new value to an existing key replaces its old value.
    # It does not create a second entry with the same key.
    print("Two medium ABU blouses were issued.")
    inventory["ABU blouse - medium"] -= 2

    print(f"Inventory after update:  {inventory}")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print(f"Inventory before deletion: {inventory}")

    # Removing a key also removes its associated value from the dictionary.
    # pop() returns the removed value so it can be displayed.
    removed_quantity = inventory.pop("Service coat - medium")

    print(f"Removed service coat entry; it had {removed_quantity} available.")
    print(f"Inventory after deletion:  {inventory}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # get() returns None for a missing key instead of raising a KeyError.
    missing_item = "ABU blouse - small"
    missing_quantity = inventory.get(missing_item)

    if missing_quantity is None:
        print(f"Missing lookup: '{missing_item}' is not in the inventory.")

    # Providing a default to pop() prevents a KeyError for a missing key.
    removed_item = inventory.pop("Service coat - large", None)

    if removed_item is None:
        print("Missing deletion: no large service coat entry was removed.")

    # A quantity of zero means the item exists but is currently out of stock.
    # Checking against None keeps zero distinct from a missing entry.
    inventory["Flight cap - medium"] = 0
    cap_quantity = inventory.get("Flight cap - medium")

    if cap_quantity is not None:
        print(f"Out-of-stock item: Flight cap - medium has {cap_quantity} available.")

    # Assigning a value to a missing key inserts a new entry.
    inventory["Flight cap - large"] = 2
    print(
        "New item added: Flight cap - large has "
        f"{inventory['Flight cap - large']} available."
    )

    # An empty dictionary contains no keys; get() safely returns None.
    empty_inventory = {}
    print(f"Empty inventory lookup: {empty_inventory.get('ABU blouse - medium')}")
    print("The result is None because the empty inventory has no entries.")

    # Python handles collisions internally. A collision occurs when different
    # keys have the same hash or compete for a location in the table.
    # Collisions can require extra work, but distinct keys remain separate.

    print("\n=== FINAL INVENTORY ===")
    for item, quantity in inventory.items():
        print(f"  {item}: {quantity} available")

if __name__ == "__main__":
    main()
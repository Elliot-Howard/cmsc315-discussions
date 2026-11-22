# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.
# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment used Python dictionaries to demonstrate hash table behavior.
The program modeled a Civil Air Patrol uniform inventory, where each key
identified a uniform item and size, and each value represented the quantity
available.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Program Design

The program created an empty dictionary named `inventory` and added five
uniform entries. Each entry paired an item and size with the number available.

The program then demonstrated these operations:

- **Insert:** Added uniform items and their quantities to the dictionary.
- **Lookup:** Retrieved the quantities for a medium ABU blouse and a small
  flight cap.
- **Update:** Reduced the number of medium ABU blouses after two were issued.
  Assigning the updated value to the existing key replaced its previous value
  rather than creating a duplicate entry.
- **Delete:** Removed the medium service coat entry using `pop()` and displayed
  the quantity that had been associated with it.

The program displayed the dictionary before and after the update and deletion
operations. It also displayed the final inventory.

## Hash Table Concepts

Python dictionaries used keys and their hash values to help locate entries.
Lookup, insertion, and deletion typically had an average time complexity of
O(1), although individual operations could take longer.

Collisions occurred when different keys had the same hash or competed for a
location in the underlying table. Python handled collisions internally so that
distinct keys could remain separate. Collisions could require additional work
to find an entry, reducing lookup efficiency. In the worst case, lookup could
take O(n) time.

## Edge Cases

The program demonstrated the following cases:

- **Missing lookup:** `get()` returned `None` for an item that was not in the
  dictionary instead of raising a `KeyError`.
- **Missing deletion:** `pop()` used `None` as a default value, so attempting
  to remove a nonexistent item did not raise a `KeyError`.
- **Zero quantity:** A medium flight cap entry had a quantity of `0`. The
  program checked against `None` so that an existing item with zero available
  was not mistaken for a missing item.
- **New key assignment:** Assigning a quantity to a missing key added a new
  entry rather than updating an existing one.
- **Empty dictionary:** A lookup with `get()` returned `None` because the
  empty dictionary contained no entries.

## Real-World Use
The inventory scenario demonstrated how a supply officer could associate
uniform items and sizes with quantities. A dictionary made it possible to
look up an item, update its quantity after issuing uniforms, and remove an
entry when it was no longer tracked.

A larger inventory application would also need features such as input
validation and persistent storage. This demonstration kept the data only
while the program was running.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your
initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the
following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables
   can improve efficiency.

### Reflection Draft

While completing this assignment, I practiced using a Python dictionary to
insert, retrieve, update, and delete key-value pairs. I used a CAP uniform
inventory as my example because the item and size could serve as a key while
the available quantity served as its value. One challenge was distinguishing
an item that was not in the dictionary from an item with a quantity of zero.
I addressed this by using `get()` and checking whether the result was `None`,
rather than treating zero as a missing value. I also used `pop()` with a
default value to avoid an error when deleting a missing entry.

A hash table uses a key's hash to help locate its associated value. A collision
occurs when different keys have the same hash or compete for a table location.
Python handles collisions internally, but resolving them can require extra
work. Dictionary operations are typically O(1) on average, making them useful
for quickly finding an inventory item without checking every entry. In the
worst case, a lookup can take O(n).
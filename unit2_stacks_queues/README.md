[# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.


## My Implementation

In this assignment, I implemented stack and queue data structures in Python. I used a Python list for the stack and the collections.deque class for the queue. The program demonstrated how stacks follow Last-In, First-Out (LIFO) and queues follow First-In, First-Out (FIFO).

## Stack Implementation

I implemented push(), pop(), peek(), and is_empty() methods. I tested the stack by adding four values and removing them in reverse order. I also tested popping and peeking when the stack was empty.

## Queue Implementation

I implemented enqueue(), dequeue(), front(), and is_empty() methods. I tested the queue by adding four values and removing them in the same order they were added. I also tested operations on an empty queue.

## Edge Cases

I tested empty stacks and queues to make sure the program handled invalid removal and viewing operations without crashing. Both structures returned None when an operation required an item but the structure was empty.

I also created single-item stacks and queues, removed their only items, and verified that both structures became empty.

## Real-World Application

I created a support desk example that used a queue to process incoming support tickets in the order they arrived. I also used a stack to record completed actions and demonstrate how the most recent action could be undone first.

## Time and Space Complexity

I used list.append() and list.pop() for the stack, which had O(1) amortized time complexity for insertion and O(1) time complexity for removal.

I used deque.append() and deque.popleft() for the queue, which provided O(1) time complexity for adding and removing items.

Both structures required O(n) memory as the number of stored items increased.

## Reflection

Completing this assignment helped me understand how stacks and queues work and how they can be used in real-world applications. I learned how to implement both data structures in Python using a list for the stack and deque for the queue. I also learned how methods such as push, pop, enqueue, and dequeue determine the order in which data is processed.

One challenge was making sure the program handled empty stacks and queues without causing errors. I addressed this by checking whether each structure was empty before removing or viewing an item. I tested these situations by trying to remove items from empty structures and by creating structures with only one item. These tests helped me verify that the methods worked correctly.

The main difference between stacks and queues is how they organize and remove data. Stacks follow Last-In, First-Out (LIFO), which means the most recently added item is removed first. This is useful for undo functions in text editors. Queues follow First-In, First-Out (FIFO), which means the first item added is removed first. This is useful for processing support tickets in the order they arrive.]()
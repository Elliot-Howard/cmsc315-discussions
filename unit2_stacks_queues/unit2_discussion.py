
"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # New values go on top, so the newest value is removed first (LIFO).
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # The last list item is the top of the stack.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New values enter at the back; older values leave first (FIFO).
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # The first item is next in line and stays in the queue.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")

    stack = Stack()

    for value in [10, 20, 30, 40]:
        stack.push(value)
        print(f"Pushed {value} onto the stack.")

    print(f"Top value before removal: {stack.peek()}")
    print("Removing values in LIFO order:")

    while not stack.is_empty():
        print(f"Popped: {stack.pop()}")

    print(f"Is stack empty? {stack.is_empty()}")
    print(f"Pop from empty stack: {stack.pop()}")
    print(f"Peek at empty stack: {stack.peek()}")

    print("\nSingle-item stack test:")
    single_stack = Stack()
    single_stack.push(99)
    print(f"Popped only item: {single_stack.pop()}")
    print(f"Is stack empty afterward? {single_stack.is_empty()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    queue = Queue()

    for value in [10, 20, 30, 40]:
        queue.enqueue(value)
        print(f"Enqueued {value} into the queue.")

    print(f"Front value before removal: {queue.front()}")
    print("Removing values in FIFO order:")

    while not queue.is_empty():
        print(f"Dequeued: {queue.dequeue()}")

    print(f"Is queue empty? {queue.is_empty()}")
    print(f"Dequeue from empty queue: {queue.dequeue()}")
    print(f"Front of empty queue: {queue.front()}")

    print("\nSingle-item queue test:")
    single_queue = Queue()
    single_queue.enqueue(99)
    print(f"Dequeued only item: {single_queue.dequeue()}")
    print(f"Is queue empty afterward? {single_queue.is_empty()}")

    # ===============================
    # TODO (Student): REAL-WORLD SCENARIO
    # ===============================
    # A support desk uses a queue to handle tickets in arrival order.
    # A stack records completed actions so the latest can be undone first.

    print("\n=== REAL-WORLD SCENARIO: SUPPORT DESK ===")

    tickets = Queue()
    action_history = Stack()

    for ticket in ["Password Reset", "Printer Issue", "Wi-Fi Problem"]:
        tickets.enqueue(ticket)
        print(f"New support ticket: {ticket}")

    print(f"\nNext ticket to process: {tickets.front()}")

    while not tickets.is_empty():
        ticket = tickets.dequeue()
        print(f"Processing ticket: {ticket}")
        action_history.push(ticket)

    print("\nUndoing the most recent completed action:")
    print(f"Undo: {action_history.pop()}")

    print(f"Next action available to undo: {action_history.peek()}")


if __name__ == "__main__":
    main()

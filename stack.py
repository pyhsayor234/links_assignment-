# ==============================
# STACK IMPLEMENTATION (LINKED LIST)
# ==============================

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, value):
        """Add an item to the top of the stack"""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """Remove and return the top item"""
        if self.is_empty():
            return "Stack is empty"
        
        removed = self.top
        self.top = self.top.next
        self._size -= 1
        return removed.value

    def peek(self):
        """Return the top item without removing it"""
        if self.is_empty():
            return "Stack is empty"
        return self.top.value

    def is_empty(self):
        """Check if stack is empty"""
        return self.top is None

    def size(self):
        """Return number of elements"""
        return self._size


# ==============================
# 1. REVERSE STRING USING STACK
# ==============================

def reverse_string(text):
    stack = Stack()
    
    for char in text:
        stack.push(char)
    
    reversed_text = ""
    while not stack.is_empty():
        reversed_text += stack.pop()
    
    return reversed_text


# ==============================
# 2. CHECK BALANCED PARENTHESES
# ==============================

def is_balanced(expression):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty():
                return False
            top = stack.pop()
            if top != pairs[char]:
                return False
    
    return stack.is_empty()


# ==============================
# 3. UNDO SYSTEM USING STACK
# ==============================

class UndoSystem:
    def __init__(self):
        self.stack = Stack()

    def perform_action(self, action):
        print(f"Performing: {action}")
        self.stack.push(action)

    def undo(self):
        if self.stack.is_empty():
            print("Nothing to undo")
        else:
            last_action = self.stack.pop()
            print(f"Undoing: {last_action}")


# ==============================
# EXAMPLE USAGE
# ==============================

if __name__ == "__main__":
    # Stack test
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    print("Top:", s.peek())   # 30
    print("Pop:", s.pop())    # 30
    print("Size:", s.size())  # 2

    print("\n--- Reverse String ---")
    print(reverse_string("hello"))  # olleh

    print("\n--- Balanced Parentheses ---")
    print(is_balanced("(a + b)"))   # True
    print(is_balanced("{[(])}"))    # False

    print("\n--- Undo System ---")
    u = UndoSystem()
    u.perform_action("Type A")
    u.perform_action("Type B")
    u.perform_action("Delete B")

    u.undo()
    u.undo()
    u.undo()
    u.undo()


# ==============================
# PART 4 — SHORT ANSWERS
# ==============================

# Why are push and pop O(1) in a stack?
# Because they only operate on the top element.
# No traversal is needed, so the time does not depend on stack size.

# What makes a stack different from a queue?
# Stack: LIFO (Last In, First Out)
# Queue: FIFO (First In, First Out)

# Name two real-world systems that use stack behavior.
# 1. Undo/Redo in applications
# 2. Call stack in programming (function calls)
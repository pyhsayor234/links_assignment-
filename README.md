# Stack Implementation Using Linked List

## 📌 Overview

This project implements a **Stack Data Structure** using a **Linked List** in Python.
It also demonstrates practical applications of stacks such as:

* Reversing a string
* Checking balanced parentheses
* Simulating an undo system

---

## 🧱 Stack Implementation

The stack is built using:

* A `Node` class (for linked list elements)
* A `Stack` class with core operations:

  * `push(value)`
  * `pop()`
  * `peek()`
  * `is_empty()`
  * `size()`

---

## ⚙️ Features

### 1. Reverse a String

Uses a stack to reverse characters in a string.

### 2. Balanced Parentheses Checker

Checks whether an expression has properly matched:

* `()`
* `{}`
* `[]`

### 3. Undo System Simulation

Simulates undo functionality using stack behavior (LIFO).

---

## ▶️ Example Usage

```python
s = Stack()

s.push(10)
s.push(20)
s.push(30)

print(s.peek())     # 30
print(s.pop())      # 30
print(s.size())     # 2
```

---

## 🧠 Key Concepts

### Why are push and pop O(1)?

Because they operate only on the top of the stack.
No traversal is required, so execution time is constant.

### Stack vs Queue

* **Stack:** Last In, First Out (LIFO)
* **Queue:** First In, First Out (FIFO)

---

## 🌍 Real-World Applications

* Undo/Redo functionality in applications
* Call stack in programming (function calls)

---

## 📂 Project Structure

```
project/
│
├── main.py        # Contains all implementations
├── README.md      # Project documentation
```

---

## 🚀 How to Run

1. Make sure Python is installed
2. Run the file:

```bash
python main.py
```

---

## 📄 License

This project is for educational purposes.

# Day 04 | Core Data Structures

## Data Structures

A **data structure** is a way of storing and organizing data so it can be accessed, modified, and managed efficiently.

Python provides **four core built-in data structures**:

* **List** – Ordered and mutable collection.
* **Tuple** – Ordered and immutable collection.
* **Set** – Unordered collection of unique values.
* **Dictionary** – Collection of key-value pairs with unique keys.

### Lists

A **List** is an ordered, mutable collection that allows duplicate values and can store multiple data types.

```python
numbers = [1, 2, 3]
```

### Tuples

A **Tuple** is an ordered and immutable collection. Once created, its elements cannot be modified.

```python
point = (10, 20)
```

### Sets

A **Set** is an unordered collection that stores only unique values. Duplicate elements are automatically removed.

```python
unique = {1, 2, 3}
```

### Dictionaries

A **Dictionary** stores data as **key-value pairs**. Each key must be unique and is used to access its corresponding value.

```python
student = {
    "name": "Ram",
    "age": 20
}
```

>> Creating Lists

Lists can be created using square brackets or the `list()` constructor.

```python
numbers = [1, 2, 3]

numbers = list((1, 2, 3))
```

>> List Length

The `len()` function returns the total number of elements in a list.

```python
len(numbers)
```

> > List Slicing

Slicing extracts a portion of a list.

```python
list[start : stop : step]
```

**Remember:**

* `start` → Starting index (inclusive)
* `stop` → Ending index (exclusive)
* `step` → Interval between elements

Example:

```python
numbers[::-1]
```

Reverses the list.

> > Common List Operations

Frequently used list methods and operations:

```python
append()
insert()
remove()
pop()
sort()
reverse()
len()
```

> > Stack (LIFO)

A **Stack** follows the **Last In, First Out (LIFO)** principle, where the most recently added element is removed first.

Common methods:

```python
append()   # Push
pop()      # Pop
```

> > Queue (FIFO)

A **Queue** follows the **First In, First Out (FIFO)** principle, where the first element added is the first one removed.

Python recommends using `collections.deque` for efficient queue operations.

```python
from collections import deque

queue = deque()
queue.append()
queue.popleft()
```

> > `collections.deque`

A **deque (Double-Ended Queue)** allows fast insertion and deletion from both the front and rear, making it more efficient than a list for queue operations.

> > Choosing the Right Data Structure

* **List** – When data needs to be modified frequently.
* **Tuple** – When data should remain unchanged.
* **Set** – When only unique values are required.
* **Dictionary** – When storing related data as key-value pairs.

> > Key Takeaway

Understanding Python's core data structures helps you choose the right way to store and manipulate data efficiently. Lists, tuples, sets, and dictionaries each have unique characteristics and are fundamental to writing efficient Python programs.
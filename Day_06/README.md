# Day 06 | Tuples and Sets

>> Theory

## Tuples

A **Tuple** is an ordered and immutable collection in Python. It can store multiple data types, allows duplicate values, and is commonly used when the data should not be changed after creation.

```python
point = (10, 20)
```

>> Creating Tuples

Tuples can be created using parentheses `()` or the `tuple()` constructor.

```python
numbers = (10, 20, 30)

numbers = tuple((10, 20, 30))
```

> > Tuple Functions

Common built-in functions used with tuples:

```python
len()
max()
min()
sum()
any()
all()
sorted()
tuple()
```

> > Tuple Packing

Tuple packing combines multiple values into a single tuple.

```python
data = 1, 2.0, "three"
```

> > Tuple Unpacking

Tuple unpacking assigns tuple elements to multiple variables.

```python
percentages = (99, 95, 90, 89, 93, 96)

a, b, c, d, e, f = percentages
```

> > Tuple Operations

### Indexing

Access an element using its index.

```python
t = (10, 20, 30)

t[1]
```

### Slicing

Extract a portion of a tuple.

```python
t = (10, 20, 30, 40)

t[1:3]
```

### Concatenation

Join two tuples using the `+` operator.

```python
t1 = (1, 2)
t2 = (3, 4)

t1 + t2
```

### Repetition

Repeat tuple elements using the `*` operator.

```python
t = (1, 2)

t * 3
```

### Membership

Check whether an element exists using the `in` operator.

```python
t = (10, 20, 30)

20 in t
```

### Comparison

Compare tuples element by element.

```python
t1 = (1, 2)
t2 = (1, 3)

t1 < t2
```

> > Tuple Immutability

Tuples are **immutable**, which means individual elements cannot be modified or deleted after the tuple is created.

```python
t = (10, 20, 30)

# Not Allowed
# del t[1]
```

The entire tuple, however, can be deleted.

```python
del t
```

---

## Sets

A **Set** is an unordered collection of unique elements. It automatically removes duplicate values and is useful when only distinct items are required.

```python
unique = {1, 2, 3}
```

>> Creating Sets

Sets can be created using curly braces `{}` or the `set()` constructor.

```python
numbers = {1, 2, 3}

numbers = set((1, 2, 3))
```

> > Set Operations

### Union (`|`)

Combines all unique elements from both sets.

```python
A = {1, 2, 3}
B = {3, 4, 5}

A | B
```

### Intersection (`&`)

Returns the common elements from both sets.

```python
A = {1, 2, 3}
B = {2, 3, 4}

A & B
```

### Difference (`-`)

Returns elements that exist in the first set but not in the second.

```python
A = {1, 2, 3}
B = {2, 4}

A - B
```

### Symmetric Difference (`^`)

Returns elements that are present in either set but not in both.

```python
A = {1, 2, 3}
B = {3, 4, 5}

A ^ B
```

### Membership

Checks whether an element exists in a set.

```python
A = {1, 2, 3}

2 in A
```

### Subset

Checks whether one set is a subset of another.

```python
A = {1, 2}
B = {1, 2, 3}

A <= B
```

> > Choosing Between Tuple and Set

* **Tuple** – Best when data should remain unchanged and order matters.
* **Set** – Best when only unique values are needed and duplicate values should be removed automatically.

> > Key Takeaway

Tuples and sets are two important Python data structures with different purposes. Tuples provide an ordered and immutable way to store related data, while sets offer an efficient way to store unique elements and perform mathematical set operations such as union, intersection, and difference.
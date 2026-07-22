# Day 14 | Python Lambda Functions, List Comprehension & Dictionary Comprehension

## 1. Python Lambda Function

A **lambda function** is a small, anonymous function in Python. Unlike a regular function defined using the `def` keyword, a lambda function is created using the `lambda` keyword.

Lambda functions are generally used for **short, simple, one-line operations** where defining a complete function using `def` may be unnecessary.

### Syntax

```python
lambda arguments: expression
```

### Example

Using a regular function:

```python
def square(x):
    return x ** 2

print(square(5))
```

Using a lambda function:

```python
square = lambda x: x ** 2

print(square(5))
```

### Output

```text
25
```

---

## 2. Lambda Function with `map()`

The `map()` function applies a given function to every item in an iterable.

Lambda functions are commonly used with `map()` to perform transformations on elements.

### Example: Convert Numbers into Squares

```python
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x ** 2, numbers))

print(result)
```

### Output

```text
[1, 4, 9, 16, 25]
```

### Explanation

Here:

* `lambda x: x ** 2` defines the operation.
* `map()` applies the operation to every number.
* `list()` converts the map object into a list.

---

## 3. Lambda Function with `filter()`

The `filter()` function is used to select elements from an iterable based on a condition.

It returns only the elements for which the given condition evaluates to `True`.

### Example: Extract Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)
```

### Output

```text
[2, 4, 6]
```

### Explanation

The lambda function checks:

```python
x % 2 == 0
```

If the condition is `True`, the number is included in the result.

---

## 4. Lambda Function with `reduce()`

The `reduce()` function repeatedly applies a function to the elements of an iterable and reduces them to a single value.

`reduce()` is available in the `functools` module.

### Example: Find the Sum of All Numbers

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a + b, numbers)

print(result)
```

### Output

```text
15
```

### How It Works

The operation is performed step by step:

```text
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15
```

---

## 5. Sorting Using Lambda Functions

Lambda functions can be used with the `key` parameter of the `sort()` method to determine how items should be sorted.

### Example: Sort a List of Tuples

```python
students = [
    ("Ram", 80),
    ("Hari", 95),
    ("Sita", 85)
]

students.sort(key=lambda x: x[1])

print(students)
```

### Output

```text
[('Ram', 80), ('Sita', 85), ('Hari', 95)]
```

Here:

```python
lambda x: x[1]
```

tells Python to sort the tuples according to the second element, which represents the student's marks.

---

## 6. Sorting a List of Dictionaries Using Lambda

Lambda functions can also be used to sort a list of dictionaries based on a specific dictionary value.

### Example

```python
employees = [
    {"name": "Ram", "salary": 50000},
    {"name": "Hari", "salary": 30000},
    {"name": "Sita", "salary": 70000}
]

employees.sort(key=lambda emp: emp["salary"])

print(employees)
```

### Output

```text
[
    {'name': 'Hari', 'salary': 30000},
    {'name': 'Ram', 'salary': 50000},
    {'name': 'Sita', 'salary': 70000}
]
```

The list is sorted according to the value of the `"salary"` key.

---

## 7. Lambda vs. Regular `def` Function

Lambda functions are not automatically faster than regular Python functions. The main difference is their **syntax and intended use**.

### Use Lambda When:

* The function is small and simple.
* The function contains a single expression.
* The function is needed temporarily.
* The function is used with functions such as `map()`, `filter()`, or `sort()`.

### Use `def` When:

* The function contains complex logic.
* Multiple statements are required.
* The function needs documentation.
* The function will be reused multiple times.
* The function is large enough to require a meaningful name.

### Example

```python
# Lambda
square = lambda x: x ** 2

# Regular function
def square(x):
    return x ** 2
```

---

# 8. Python List Comprehension

**List comprehension** is a compact way to create a new list from an existing iterable.

It combines a loop and an expression into a single line of code.

Instead of writing multiple lines using a traditional `for` loop, list comprehension allows us to perform the same operation in a concise and readable way.

### Basic Syntax

```python
[expression for item in iterable]
```

---

## 9. List Comprehension Without Condition

### Example: Create a List of Squares

```python
numbers = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in numbers]

print(squares)
```

### Output

```text
[1, 4, 9, 16, 25]
```

The expression:

```python
num ** 2
```

is applied to every element in the `numbers` list.

---

## 10. List Comprehension with a Condition

We can use an `if` condition to select only specific elements.

### Syntax

```python
[expression for item in iterable if condition]
```

### Example: Extract Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6]

evens = [num for num in numbers if num % 2 == 0]

print(evens)
```

### Output

```text
[2, 4, 6]
```

Only numbers satisfying the condition:

```python
num % 2 == 0
```

are included.

---

## 11. List Comprehension with `if-else`

List comprehension can also be used to return different values depending on a condition.

### Syntax

```python
[true_value if condition else false_value for item in iterable]
```

### Example: Identify Even and Odd Numbers

```python
numbers = [1, 2, 3, 4]

result = ["Even" if num % 2 == 0 else "Odd" for num in numbers]

print(result)
```

### Output

```text
['Odd', 'Even', 'Odd', 'Even']
```

---

## 12. Nested List Comprehension

List comprehension can contain more than one `for` loop.

### Example

```python
list1 = [1, 2]
list2 = ["A", "B"]

pairs = [(x, y) for x in list1 for y in list2]

print(pairs)
```

### Output

```text
[(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
```

The inner loop runs for every element of the outer loop.

---

# 13. Python Dictionary Comprehension

**Dictionary comprehension** is a concise way to create dictionaries using a single line of code.

### Basic Syntax

```python
{key: value for item in iterable}
```

Dictionary comprehension allows us to generate key-value pairs efficiently.

---

## 14. Dictionary Comprehension with a Condition

We can use an `if` condition to include only selected elements.

### Example: Create a Dictionary of Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6]

result = {
    num: num ** 2
    for num in numbers
    if num % 2 == 0
}

print(result)
```

### Output

```text
{2: 4, 4: 16, 6: 36}
```

Here:

* The number becomes the **key**.
* The square of the number becomes the **value**.
* Only even numbers are included.

---

## 15. Dictionary Comprehension with an Existing Dictionary

We can use `.items()` to iterate over the key-value pairs of an existing dictionary.

### Example: Select Students with Even Marks

```python
original_dict = {
    "ram": 38,
    "sita": 48,
    "gita": 57,
    "john": 33
}

even_dict = {
    k: v
    for k, v in original_dict.items()
    if v % 2 == 0
}

print(even_dict)
```

### Output

```text
{'ram': 38, 'sita': 48}
```

Only dictionary entries whose values are even are selected.

---

## 16. Multiple Conditions in Dictionary Comprehension

Multiple conditions can be used in dictionary comprehension.

### Example

```python
original_dict = {
    "Dhiraj": 38,
    "Ram": 48,
    "sita": 57,
    "john": 33
}

new_dict = {
    k: v
    for k, v in original_dict.items()
    if v % 2 != 0
    if v < 40
}

print(new_dict)
```

### Output

```text
{'john': 33}
```

The result contains values that satisfy both conditions:

```python
v % 2 != 0
```

and

```python
v < 40
```

---

## 17. Dictionary Comprehension with `if-else`

We can use `if-else` in dictionary comprehension to assign different values based on a condition.

### Syntax

```python
{
    key: value_if_true if condition else value_if_false
    for item in iterable
}
```

### Example: Label Numbers as Even or Odd

```python
numbers = [1, 2, 3, 4, 5]

result = {
    num: "Even" if num % 2 == 0 else "Odd"
    for num in numbers
}

print(result)
```

### Output

```text
{
    1: 'Odd',
    2: 'Even',
    3: 'Odd',
    4: 'Even',
    5: 'Odd'
}
```

---

# 18. Quick Comparison

| Concept                  | Purpose                              | Example                      |
| ------------------------ | ------------------------------------ | ---------------------------- |
| `lambda`                 | Create a small anonymous function    | `lambda x: x ** 2`           |
| `map()`                  | Transform every element              | Square every number          |
| `filter()`               | Select elements based on a condition | Select even numbers          |
| `reduce()`               | Reduce multiple values to one result | Calculate total              |
| `list.sort()`            | Sort elements                        | Sort students by marks       |
| List Comprehension       | Create or transform lists concisely  | `[x**2 for x in numbers]`    |
| Dictionary Comprehension | Create dictionaries concisely        | `{x: x**2 for x in numbers}` |

---

# 19. Summary

* **Lambda functions** are small, anonymous, one-line functions.
* Lambda functions are commonly used with `map()`, `filter()`, and sorting.
* `map()` is used to transform elements.
* `filter()` is used to select elements based on a condition.
* `reduce()` combines elements into a single result.
* Lambda functions are not necessarily faster than regular `def` functions.
* **List comprehension** provides a concise way to create and transform lists.
* List comprehension can be used with conditions and `if-else`.
* **Dictionary comprehension** provides a concise way to create dictionaries.
* Dictionary comprehension can also use conditions and `if-else`.
* Choosing between lambda and `def` depends mainly on the complexity and reusability of the function.

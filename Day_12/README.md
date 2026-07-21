# Day 12 | Docstrings, `*args` and `**kwargs` in Python

--- 
# Docstrings in Python

## What is a Docstring?

A **docstring**, short for **documentation string**, is a string used to document a function, class, or module.

It explains what a function does and can provide information about:

* The purpose of the function
* The parameters it accepts
* The value it returns

A docstring is written inside triple quotes (`""" """`) and is placed immediately after the function definition.

### Syntax

```python
def function_name():
    """
    Function description.
    """
    
    # Function code
```

---

## Example of a Docstring

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    length (float): Length of the rectangle.
    width (float): Width of the rectangle.

    Returns:
    float: Area of the rectangle.
    """
    return length * width
```

In this example:

* `calculate_area()` is the function.
* The text inside `""" """` is the **docstring**.
* The `Parameters` section describes the inputs.
* The `Returns` section describes the output.

---

## Accessing Documentation

A function's docstring can be accessed using the `__doc__` attribute.

```python
print(calculate_area.__doc__)
```

Python's built-in `help()` function can also be used to display documentation about a function.

```python
help(calculate_area)
```

The `__doc__` attribute and `help()` function provide ways to access the documentation written inside a function.

---

# Comment vs Docstring

A common interview question is:

> **What is the difference between a comment and a docstring?**

| Comment                                                   | Docstring                                        |
| --------------------------------------------------------- | ------------------------------------------------ |
| Used to explain code internally                           | Used to document functions, classes, and modules |
| Starts with `#`                                           | Usually written using triple quotes `""" """`    |
| Mainly helps developers understand specific parts of code | Provides documentation for program components    |
| Not accessed as function documentation                    | Can be accessed using `__doc__` and `help()`     |

### Comment Example

```python
# Calculate the area of the rectangle
area = length * width
```

### Docstring Example

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    """
    return length * width
```

The key difference is that **comments explain code**, while **docstrings provide structured documentation for functions, classes, and modules**.

---

# `*args` in Python

## What is `*args`?

The special syntax `*args` allows a function to accept an **arbitrary number of positional arguments**.

The positional arguments passed to `*args` are collected into a **tuple**. This is useful when we do not know in advance how many positional arguments will be passed to the function.

### Syntax

```python
def function_name(*args):
    # Function code
```

The name `args` is a convention. The important part is the `*` symbol.

For example, the following also works:

```python
def function_name(*numbers):
    # Function code
```

However, using `*args` is the common Python convention.

---

## Example of `*args`

```python
def myFun(*args):
    for arg in args:
        print(arg)

myFun("Hello", "Welcome", "to", "Skill Shikshya")
```

### Output

```text
Hello
Welcome
to
Skill Shikshya
```

### Explanation

```python
def myFun(*args):
```

The function accepts any number of positional arguments.

```python
for arg in args:
```

The `for` loop goes through each value stored in the `args` tuple.

The values passed to the function are collected as:

```python
("Hello", "Welcome", "to", "Skill Shikshya")
```

Therefore, we can loop through `args` and process each argument individually.

---

## Practical Example of `*args`

The `*args` syntax can be useful when performing an operation on an unknown number of values.

### Example: Multiplication

```python
def multiply(*args):
    result = 1

    for num in args:
        result *= num

    return result

print(multiply(2, 3, 4))
```

### Output

```text
24
```

### Explanation

```python
result = 1
```

The result is initialized to `1` because we are performing multiplication.

```python
for num in args:
```

The loop processes each number passed to the function.

```python
result *= num
```

Each number is multiplied with the current value of `result`.

Finally, the function returns the multiplication result.

---

# `**kwargs` in Python

## What is `**kwargs`?

The special syntax `**kwargs` allows a function to accept an **arbitrary number of keyword arguments**.

Keyword arguments are passed in the form:

```python
key=value
```

The arguments passed using `**kwargs` are collected into a **dictionary**.

* **Keys** → Argument names
* **Values** → Argument values

This is useful when the number of keyword arguments is not known in advance.

### Syntax

```python
def function_name(**kwargs):
    # Function code
```

Just like `args`, the name `kwargs` is a convention. The important part is the `**` symbol.

---

## Example of `**kwargs`

```python
def fun(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

fun(
    s1="Python",
    s2="is",
    s3="Awesome"
)
```

### Output

```text
s1 = Python
s2 = is
s3 = Awesome
```

The keyword arguments are collected into a dictionary:

```python
{
    "s1": "Python",
    "s2": "is",
    "s3": "Awesome"
}
```

The `.items()` method allows us to access both the keys and values from the dictionary.

---

## Practical Example of `**kwargs`

The `**kwargs` syntax can be used to create flexible functions that accept different types of information.

### Example

```python
def introduce(**kwargs):
    details = []

    for key, value in kwargs.items():
        details.append(key + ": " + str(value))

    return ", ".join(details)

print(
    introduce(
        Name="Alice",
        Age=25,
        City="New York"
    )
)
```

### Output

```text
Name: Alice, Age: 25, City: New York
```

### Explanation

```python
def introduce(**kwargs):
```

The function accepts any number of keyword arguments.

```python
for key, value in kwargs.items():
```

The loop accesses each key-value pair from the dictionary.

```python
details.append(key + ": " + str(value))
```

Each key-value pair is converted into a readable format and added to the `details` list.

```python
", ".join(details)
```

The list items are combined into a single string, separated by commas.

---

# Using `*args` and `**kwargs` Together

Python allows us to use both `*args` and `**kwargs` in the same function.

* `*args` collects **positional arguments** into a **tuple**.
* `**kwargs` collects **keyword arguments** into a **dictionary**.

### Example

```python
def student_info(*args, **kwargs):
    print("Subjects:", args)
    print("Details:", kwargs)

student_info(
    "Math",
    "Science",
    "English",
    Name="Alice",
    Age=20,
    City="New York"
)
```

### Output

```text
Subjects: ('Math', 'Science', 'English')
Details: {'Name': 'Alice', 'Age': 20, 'City': 'New York'}
```

Here:

```python
"Math", "Science", "English"
```

are positional arguments and are stored in `args`.

The following are keyword arguments:

```python
Name="Alice"
Age=20
City="New York"
```

These are stored in `kwargs` as a dictionary.

---

# Quick Comparison

| Feature         | `*args`                              | `**kwargs`                        |
| --------------- | ------------------------------------ | --------------------------------- |
| Full Meaning    | Variable-length positional arguments | Variable-length keyword arguments |
| Argument Type   | Positional                           | Keyword                           |
| Collection Type | Tuple                                | Dictionary                        |
| Syntax          | `*args`                              | `**kwargs`                        |
| Example         | `func(10, 20, 30)`                   | `func(name="Alice", age=20)`      |
| Access          | Loop through values                  | Loop through key-value pairs      |

### Simple Example

```python
def example(*args, **kwargs):
    print(args)
    print(kwargs)

example(10, 20, 30, name="Alice", age=20)
```

### Output

```text
(10, 20, 30)
{'name': 'Alice', 'age': 20}
```

---

# Summary

* A **docstring** is used to document functions, classes, and modules.
* Docstrings are commonly written using triple quotes (`""" """`).
* A function's docstring can be accessed using `__doc__`.
* The `help()` function can also be used to view documentation.
* **Comments** are mainly used to explain code internally.
* **Docstrings** provide documentation for program components.
* `*args` allows a function to accept an arbitrary number of **positional arguments**.
* `*args` stores positional arguments in a **tuple**.
* `**kwargs` allows a function to accept an arbitrary number of **keyword arguments**.
* `**kwargs` stores keyword arguments in a **dictionary**.
* `*args` and `**kwargs` can be used together to create flexible functions.

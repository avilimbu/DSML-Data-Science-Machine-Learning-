# Day 10 | Python Functions

---


## 📖 What is a Function?

A function is a reusable block of code that performs a specific task. Functions help organize code, reduce repetition, and make programs easier to understand and maintain.

### Benefits of Functions

- Code reusability
- Better readability
- Easier debugging
- Modular programming
- Reduced code duplication

---

## 🔹 Types of Functions

### 1. User-Defined Functions

User-defined functions are created by the programmer using the `def` keyword. They are designed to perform specific tasks according to the program's requirements.

**Example:**

```python
def add(a, b):
    return a + b

print(add(5, 6))
```

---

### 2. Built-in Functions

Built-in functions are already provided by Python. They can be used directly without defining them.

**Common Examples:**

```python
print("Hello")
len("Python")
sum([1, 2, 3])
type(10)
input("Enter your name: ")
```

---

## Function Definition

A function is defined using the `def` keyword followed by:

- Function name
- Parentheses `()`
- Parameters (optional)
- Colon `:`
- Function body

**Syntax:**

```python
def function_name(parameters):
    # function body
    return value
```

---

## Function Call

A function is executed when it is called using its name followed by parentheses.

**Example:**

```python
def greet():
    print("Welcome!")

greet()
```

---

## Function Parameters

Parameters allow values to be passed into a function.

**Example:**

```python
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)
```

---

## Return Statement

The `return` statement sends a value back to the place where the function was called.

**Example:**

```python
def square(num):
    return num * num

print(square(6))
```

---


## 📌 Conclusion

Functions are one of the most important concepts in Python programming. They make code modular, reusable, and easier to maintain. Mastering functions is essential before learning advanced topics such as recursion, object-oriented programming, and modules.
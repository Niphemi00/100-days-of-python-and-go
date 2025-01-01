# Day 5: For Loops and the `range()` Function

## Python
### 1. **For Loop Basics**
The `for` loop in Python iterates over a sequence (e.g., a list, string, or range).

#### Example:
```python
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a string
for letter in "hello":
    print(letter)
```

### 2. **The `range()` Function**
The `range()` function generates a sequence of numbers, which is often used with `for` loops.

#### Syntax:
```python
range(start, stop, step)
```
- **start**: Starting number (default is 0).
- **stop**: Ending number (exclusive).
- **step**: Step size (default is 1).

#### Example:
```python
# Basic range
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# Custom start and stop
for i in range(1, 6):
    print(i)  # Output: 1, 2, 3, 4, 5

# Custom step
for i in range(0, 10, 2):
    print(i)  # Output: 0, 2, 4, 6, 8
```

---
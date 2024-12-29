# Day 2: Data Types, Math Operations, F-Strings, Number Manipulation, and Type Conversion

## Key Topics Covered

### 1. **Data Types**
- Common data types in Python:
  - **int**: Integers, e.g., `5`, `-10`
  - **float**: Floating-point numbers, e.g., `3.14`, `-0.5`
  - **str**: Strings, e.g., `'hello'`, `'123'`
  - **bool**: Boolean values, `True` or `False`
- Checking the type of a variable using `type()`:
  ```python
  x = 42
  print(type(x))  # Output: <class 'int'>
  ```

### 2. **Math Operations**
- Arithmetic operations:
  - Addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`)
  - Floor division (`//`), modulus (`%`), and exponentiation (`**`)
- Example:
  ```python
  a = 10
  b = 3
  print(a + b)  # 13
  print(a // b)  # 3 (floor division)
  print(a ** b)  # 1000 (10 to the power of 3)
  ```

### 3. **F-Strings**
- Used for formatting strings with embedded variables.
- Syntax: `f"text {variable}"`
- Example:
  ```python
  name = "Alice"
  age = 25
  print(f"My name is {name} and I am {age} years old.")
  ```

### 4. **Number Manipulation**
- Rounding numbers using `round()`:
  ```python
  result = 3.14159
  print(round(result, 2))  # 3.14
  ```
- Using floor and ceil functions from the `math` module:
  ```python
  import math
  print(math.floor(2.9))  # 2
  print(math.ceil(2.1))  # 3
  ```

### 5. **Type Conversion**
- Converting between data types:
  - `int()` to convert to an integer
  - `float()` to convert to a float
  - `str()` to convert to a string
- Example:
  ```python
  num = "100"
  converted_num = int(num)
  print(converted_num + 50)  # 150
  ```

## Key Takeaways
- Python has versatile data types and operations to handle numbers and strings efficiently.
- F-strings simplify string formatting with variables.
- Understanding type conversion is crucial when working with mixed data types.

## Challenges Faced
- Misusing the `round()` function by forgetting to specify the number of decimal places.
- Trying to perform arithmetic operations on strings without conversion.

## Practice Questions
1. Write a program that takes two numbers, adds them, and prints the result using an f-string.
2. Perform floor division and modulus operations on two numbers and display the results.
3. Convert the string `'3.14'` to a float and multiply it by 2.
4. Debug the following code:
   ```python
   age = "30"
   print("Next year, you will be " + age + 1)
   ```

# PROJECT TWO : BILL CALCULATOR
# Day 1: Strings, Debugging, Concatenation, Manipulation, and Variables

## Key Topics Covered
1. **Variables**: Learned how to declare and assign variables in Python.
   - Syntax: `variable_name = value`
   - Example:
     ```python
     name = "John"
     age = 25
     ```

2. **Strings**:
   - Strings are sequences of characters enclosed in quotes (`"` or `'`).
   - Example:
     ```python
     greeting = "Hello, World!"
     ```

3. **String Concatenation**:
   - Combining multiple strings using the `+` operator.
   - Example:
     ```python
     first_name = "John"
     last_name = "Doe"
     full_name = first_name + " " + last_name
     print(full_name)  # Output: John Doe
     ```

4. **String Manipulation**:
   - Methods like `.lower()`, `.upper()`, `.strip()`, and `.replace()` for modifying strings.
   - Example:
     ```python
     message = " Hello, Python! "
     print(message.strip())  # Removes leading and trailing spaces
     print(message.upper())  # Converts to uppercase
     print(message.replace("Python", "World"))  # Replaces a substring
     ```

5. **Debugging**:
   - Strategies to identify and fix errors in code.
   - Common errors include:
     - Syntax errors (e.g., missing colons or parentheses).
     - Name errors (e.g., using an undefined variable).
     - Logical errors (e.g., incorrect calculations).
   - Example:
     ```python
     # Debugging Example
     # Original Code
     print("My name is" + name)

     # Fixed Code
     name = "John"
     print("My name is " + name)
     ```

## Key Takeaways
- Variables allow storing and reusing data.
- Strings are versatile and can be manipulated easily using built-in methods.
- Debugging is an essential skill for identifying and fixing errors.

## Challenges Faced
- Forgetting to add spaces during string concatenation.
- Misusing string methods, such as trying to use `.strip()` on an integer.

## Practice Questions
1. Create a variable to store your name and print a greeting using string concatenation.
2. Write a program that takes a string, converts it to uppercase, and replaces a word in it.
3. Debug the following code:
   ```python
   city = "New York"
   print("I live in" city)
   ```

## Project 1: BANDNAME GENERATOR USING THE INPUT FUNCTION
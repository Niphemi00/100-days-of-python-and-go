# Day 1: Strings, Debugging, Concatenation, Manipulation, and Variables in Go

## Key Topics Covered
1. **Variables**: Learned how to declare and assign variables in Go.
   - Syntax: `var variableName type = value` or shorthand `variableName := value`
   - Example:
     ```go
     var name string = "John"
     age := 25
     ```

2. **Strings**:
   - Strings are sequences of characters enclosed in double quotes (`"`).
   - Example:
     ```go
     greeting := "Hello, World!"
     fmt.Println(greeting)
     ```

3. **String Concatenation**:
   - Combining multiple strings using the `+` operator.
   - Example:
     ```go
     firstName := "John"
     lastName := "Doe"
     fullName := firstName + " " + lastName
     fmt.Println(fullName)  // Output: John Doe
     ```

4. **String Manipulation**:
   - Functions from the `strings` package like `ToLower`, `ToUpper`, `TrimSpace`, and `Replace` for modifying strings.
   - Example:
     ```go
     import "strings"

     message := " Hello, Go! "
     fmt.Println(strings.TrimSpace(message))  // Removes leading and trailing spaces
     fmt.Println(strings.ToUpper(message))    // Converts to uppercase
     fmt.Println(strings.Replace(message, "Go", "World", 1))  // Replaces a substring
     ```

5. **Debugging**:
   - Strategies to identify and fix errors in code.
   - Common errors include:
     - Syntax errors (e.g., missing semicolons or incorrect use of braces).
     - Logical errors (e.g., incorrect calculations or conditions).
   - Example:
     ```go
     // Debugging Example
     // Original Code
     fmt.Println("My name is" + name)

     // Fixed Code
     name := "John"
     fmt.Println("My name is " + name)
     ```

## Key Takeaways
- Variables allow storing and reusing data in Go.
- Strings are versatile and can be manipulated using functions from the `strings` package.
- Debugging is an essential skill for identifying and fixing errors.

## Challenges Faced
- Forgetting to add spaces during string concatenation.
- Misusing string functions, such as trying to use `TrimSpace` on an integer.

## Practice Questions
1. Create a variable to store your name and print a greeting using string concatenation.
2. Write a program that takes a string, converts it to uppercase, and replaces a word in it.
3. Debug the following code:
   ```go
   city := "New York"
   fmt.Println("I live in" city)
   ```

# PROJECT ONE : BANDNAME GENERATOR
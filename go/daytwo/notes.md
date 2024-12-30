# Day 2: Data Types, Math Operations, F-Strings (fmt.Sprintf), Number Manipulation, and Type Conversion in Go

## Key Topics Covered

### 1. **Data Types**
- Common data types in Go:
  - **int**: Integers, e.g., `5`, `-10`
  - **float64**: Floating-point numbers, e.g., `3.14`, `-0.5`
  - **string**: Strings, e.g., `"hello"`, `"123"`
  - **bool**: Boolean values, `true` or `false`
- Checking the type of a variable using `%T` in `fmt.Printf`:
  ```go
  x := 42
  fmt.Printf("%T\n", x)  // Output: int
  ```

### 2. **Math Operations**
- Arithmetic operations:
  - Addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`)
  - Modulus (`%`)
- Example:
  ```go
  a := 10
  b := 3
  fmt.Println(a + b)  // 13
  fmt.Println(a / b)  // 3 (integer division)
  fmt.Println(a % b)  // 1 (remainder)
  ```

### 3. **F-Strings Equivalent (fmt.Sprintf)**
- Used for formatting strings with embedded variables.
- Syntax: `fmt.Sprintf("text %v", variable)`
- Example:
  ```go
  name := "Alice"
  age := 25
  greeting := fmt.Sprintf("My name is %s and I am %d years old.", name, age)
  fmt.Println(greeting)
  ```

### 4. **Number Manipulation**
- Rounding numbers using `math.Round`:
  ```go
  import "math"

  result := 3.14159
  fmt.Println(math.Round(result*100) / 100)  // 3.14
  ```
- Using `math.Floor` and `math.Ceil`:
  ```go
  fmt.Println(math.Floor(2.9))  // 2
  fmt.Println(math.Ceil(2.1))   // 3
  ```

### 5. **Type Conversion**
- Converting between data types:
  - `int()` to convert to an integer
  - `float64()` to convert to a float
  - `strconv.Itoa()` to convert an integer to a string
- Example:
  ```go
  import "strconv"

  num := 100
  strNum := strconv.Itoa(num)
  fmt.Println("The number is " + strNum)
  ```

## Key Takeaways
- Go has strong static typing, requiring explicit type conversions when needed.
- `fmt.Sprintf` is a powerful tool for creating formatted strings.
- The `math` package provides helpful functions for number manipulation.

## Challenges Faced
- Understanding the difference between integer and floating-point division.
- Forgetting to import required packages like `math` or `strconv`.

## Practice Questions
1. Write a program that takes two numbers, adds them, and prints the result using `fmt.Sprintf`.
2. Perform modulus operations on two numbers and display the result.
3. Convert the string `"3.14"` to a float and multiply it by 2.
4. Debug the following code:
   ```go
   age := "30"
   fmt.Println("Next year, you will be " + age + 1)
   ```

# PROJECT TWO : BILL CALCULATOR
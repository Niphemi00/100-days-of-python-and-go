## Go Notes

### Key Topics Covered

#### 1. **Control Flow**
- **if, else if, else Statements**:
  - Syntax:
    ```go
    if condition1 {
        // code block
    } else if condition2 {
        // code block
    } else {
        // code block
    }
    ```
  - Example:
    ```go
    age := 18
    if age < 18 {
        fmt.Println("You are a minor.")
    } else if age == 18 {
        fmt.Println("You just became an adult!")
    } else {
        fmt.Println("You are an adult.")
    }
    ```

#### 2. **Operators**
- **Comparison Operators**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical Operators**: `&&`, `||`, `!`
- Example:
  ```go
  x := 10
  y := 20
  if x < y && y > 15 {
      fmt.Println("Both conditions are true.")
  }
  ```

### Challenges Faced
- Remembering to use `{}` even for single-line if statements.

### Practice Questions
1. Write a program to check if a number is odd or even.
2. Write a program to check if a string contains a specific substring.

## PROJECT THREE: TREASURE ISLAND GAME

## Go
### 1. **For Loop Basics**
In Go, the `for` loop is the only looping construct but can be used in various ways.

#### Example:
```go
package main
import "fmt"

func main() {
    // Iterating over a slice
    fruits := []string{"apple", "banana", "cherry"}
    for _, fruit := range fruits {
        fmt.Println(fruit)
    }

    // Iterating over a string
    for _, letter := range "hello" {
        fmt.Printf("%c\n", letter)
    }
}
```

### 2. **Range in Go**
The `range` keyword is used to iterate over slices, arrays, maps, strings, and channels.

#### Example:
```go
package main
import "fmt"

func main() {
    // Iterating over a slice
    numbers := []int{0, 1, 2, 3, 4}
    for index, value := range numbers {
        fmt.Printf("Index: %d, Value: %d\n", index, value)
    }

    // Iterating over a map
    colors := map[string]string{"R": "Red", "G": "Green", "B": "Blue"}
    for key, value := range colors {
        fmt.Printf("Key: %s, Value: %s\n", key, value)
    }

    // Using a basic for loop (similar to Python's range)
    for i := 0; i < 5; i++ {
        fmt.Println(i) // Output: 0, 1, 2, 3, 4
    }
}
```

---

### Key Differences:
1. **Python**:
   - The `range()` function is explicitly used to generate sequences.
   - For loops can iterate over any iterable (list, string, etc.).

2. **Go**:
   - The `range` keyword is versatile for iterating over various data structures.
   - The `for` loop can also mimic a C-style loop by defining start, stop, and step directly.


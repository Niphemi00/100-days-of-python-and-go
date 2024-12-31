 # Lists and Randomization in Python and Go

This note provides an overview of handling lists and performing randomization in both Python and Go.

---

## Python: Lists and Randomization

### Lists in Python
A **list** in Python is an ordered collection of items that can hold elements of any data type.

#### Common Operations on Lists
- **Creating a List:**
  ```python
  my_list = [1, 2, 3, 4, 5]
  ```

- **Accessing Elements:**
  ```python
  print(my_list[0])  # Output: 1
  print(my_list[-1]) # Output: 5
  ```

- **Modifying Elements:**
  ```python
  my_list[1] = 10
  print(my_list)  # Output: [1, 10, 3, 4, 5]
  ```

- **Appending and Removing Elements:**
  ```python
  my_list.append(6)  # Add to the end
  my_list.remove(3)  # Remove specific element
  print(my_list)  # Output: [1, 10, 4, 5, 6]
  ```

### Randomization in Python
Python provides the `random` module for randomization.

#### Key Functions in `random`
- **`random.choice`**: Selects a random item from a list.
  ```python
  import random
  items = ["apple", "banana", "cherry"]
  print(random.choice(items))
  ```

- **`random.shuffle`**: Shuffles a list in place.
  ```python
  random.shuffle(items)
  print(items)
  ```

- **`random.sample`**: Returns a new list of random items.
  ```python
  print(random.sample(items, 2))
  ```

- **Random Numbers in Ranges:**
  ```python
  print(random.randint(1, 10))  # Integer between 1 and 10
  print(random.uniform(0, 1))  # Float between 0.0 and 1.0
  ```

---

# Time and Space Complexity Analysis

This repository contains an activity focused on analyzing different Python code snippets to determine their **Time Complexity** and **Space Complexity** using Big-O notation.

## Student Details

| Detail | Information |
|---|---|
| **Author** | **Aayush Singh** |
| **Roll Number** | IC-2K24-04 |
| **Subject** | Data Structures and Algorithms |
| **Activity** | Time and Space Complexity Analysis |
| **Language** | Python |

## Objective

The objective of this activity is to understand and analyze the efficiency of different algorithms by calculating their time and space complexity using Big-O notation.

## Complexity Analysis

### 1. Find Maximum Element

**Problem:** Find the maximum element in a given array.

**Code:**

    def find_max(arr):
        max_val = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > max_val:
                max_val = arr[i]
        return max_val

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

**Justification:** The loop checks each element of the array once, taking linear time. Only a few variables are used, requiring constant extra space.

### 2. Check for Duplicate Elements

**Problem:** Check whether an array contains any duplicate elements.

**Code:**

    def has_duplicate(arr):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]:
                    return True
        return False

- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)

**Justification:** The two nested loops compare possible pairs of elements, resulting in quadratic time complexity. Only loop variables are used, requiring constant extra space.

### 3. Factorial Using Recursion

**Problem:** Calculate the factorial of a number using recursion.

**Code:**

    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

**Justification:** The function makes one recursive call for each value from n down to 1, resulting in linear time complexity. The recursion stack can contain up to n calls, requiring linear space.

### 4. Fibonacci Using Recursion

**Problem:** Calculate the Fibonacci number using recursion.

**Code:**

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

- **Time Complexity:** O(2^n)
- **Space Complexity:** O(n)

**Justification:** Each function call generates two additional recursive calls (n-1 and n-2), resulting in exponential time complexity. The maximum recursion depth is n, requiring linear stack space.

## Summary Table

| Snippet | Problem | Time Complexity | Space Complexity |
|---|---|---|---|
| 1 | Find Maximum Element | O(n) | O(1) |
| 2 | Check for Duplicates | O(n²) | O(1) |
| 12 | Factorial Using Recursion | O(n) | O(n) |
| 13 | Fibonacci Using Recursion | O(2^n) | O(n) |

## Key Concepts

- **O(1):** Constant complexity; execution or memory usage does not grow with input size.
- **O(n):** Linear complexity; grows proportionally with input size.
- **O(n²):** Quadratic complexity; commonly occurs with nested loops.
- **O(2^n):** Exponential complexity; commonly occurs in naive recursive algorithms such as Fibonacci.

## Conclusion

Analyzing time and space complexity helps determine how efficiently an algorithm performs as the input size increases.

Simple loops may have linear complexity, nested loops can lead to quadratic complexity, and recursive algorithms may require additional stack space and significantly higher execution time.

This activity provides a basic understanding of algorithm analysis and the importance of writing efficient programs.

---

**Author:** Aayush Singh
**Roll Number:** IC-2K24-04

*Time and Space Complexity Analysis | Practical Activity*

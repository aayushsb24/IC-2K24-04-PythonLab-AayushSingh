# Python Programming Lab – Algorithm Analysis

## Performance Comparison of Naive and Optimized Algorithms

### Objective

To implement and compare different approaches for solving computational problems using Python. The assignment focuses on understanding how algorithm optimization improves execution time and resource efficiency.

The programs compare naive approaches with optimized algorithms using mathematical techniques, sorting, binary search, and hash maps.

---

## Technologies Used

- Python 3.x
- `time` module
- `random` module
- Dictionaries (Hash Maps)
- Visual Studio Code

---

## Programs Included

1. Sum of Prime Numbers
2. Count Pairs with a Given Sum
3. Kth Smallest Pair Sum

---

## 1. Sum of Prime Numbers

### Objective

To calculate the sum of all prime numbers less than a given integer `N` using three different approaches.

### Methods Implemented

**Method 1: Naive Prime Summation**

- Checks every number from 2 to N-1.
- Tests divisibility using all numbers from 2 to x-1.
- Adds the number to the total if it is prime.

**Method 2: Square Root Optimization**

- Checks divisibility only up to the square root of the number.
- Skips even numbers greater than 2.
- Reduces unnecessary divisibility checks.

**Method 3: Sieve of Eratosthenes**

- Uses a Boolean list to identify prime numbers.
- Eliminates multiples of each prime number.
- Calculates the sum of all remaining prime numbers.

### Complexity Comparison

| Method | Time Complexity | Space Complexity |
|---|---|---|
| Naive | O(N²) | O(1) |
| Square Root Optimization | O(N√N) | O(1) |
| Sieve of Eratosthenes | O(N log log N) | O(N) |

### Test Cases

| Input (N) | Expected Sum |
|---|---:|
| 10 | 17 |
| 30 | 129 |
| 100 | 1060 |
| 1000 | 76127 |

### Performance Analysis

The naive approach becomes increasingly slow as the input size grows because it performs repeated divisibility checks.

The square root method reduces the number of checks, while the Sieve of Eratosthenes provides much better performance for large input values by identifying all prime numbers together.

---

## 2. Count Pairs with a Given Sum

### Objective

To count the number of unique index pairs in an array whose elements add up to a specified target value.

### Methods Implemented

**Method 1: Naive Approach**

- Uses two nested loops to examine every possible pair.
- Checks whether the sum of the two elements equals the target.
- Increments the count whenever a matching pair is found.

**Method 2: Optimized Approach Using Hash Map**

- Uses a dictionary to store previously encountered numbers and their frequencies.
- Calculates the complement of each number using `target - x`.
- Checks whether the complement already exists in the dictionary.
- Updates the pair count using the stored frequency.
- Stores the current number and updates its frequency.

### Complexity Comparison

| Method | Time Complexity | Space Complexity |
|---|---|---|
| Naive Approach | O(N²) | O(1) |
| Optimized Hash Map | O(N) average | O(N) |

### Input Details

- Array size: 5,000 and 50,000
- Random number range: 1 to 20,000
- Target sum: 20,000
- Random seed: 42

### Performance Analysis

The naive approach checks every possible pair, resulting in quadratic time complexity.

The optimized approach uses a hash map to find complementary values efficiently, reducing the average time complexity to linear time.

Both methods produce the same pair count for the same input array.

---

## 3. Kth Smallest Pair Sum

### Objective

To find the Kth smallest sum among all possible pairs of distinct elements in an array.

### Methods Implemented

**Method 1: Naive Approach**

- Generates all possible pair sums using nested loops.
- Stores the calculated sums in a list.
- Sorts the list in ascending order.
- Returns the element at position K-1.

**Method 2: Optimized Approach Using Binary Search**

- Sorts the original array.
- Determines the minimum and maximum possible pair sums.
- Uses binary search to find the required pair sum.
- Uses a two-pointer technique to count the number of pairs whose sum is less than or equal to a given value.
- Adjusts the binary search range until the Kth smallest sum is found.

### Complexity Comparison

| Method | Time Complexity | Space Complexity |
|---|---|---|
| Naive Approach | O(N² log N) | O(N²) |
| Optimized Approach | O(N log R) | O(N) |

Here, R represents the range between the minimum and maximum possible pair sums.

### Input Details

- Array size (N): 5000
- Random number range: 1 to 100000
- K value: 1000000
- Random seed: 42

### Performance Analysis

The naive approach generates and sorts every possible pair sum, requiring significant time and memory.

The optimized approach avoids generating all pair sums. Instead, it uses binary search and a two-pointer counting technique to find the required result efficiently.

Both approaches return the same Kth smallest pair sum.

---

## Overall Algorithm Comparison

| Problem | Naive Approach | Optimized Approach |
|---|---|---|
| Sum of Prime Numbers | Repeated divisibility checks | Square root optimization / Sieve |
| Count Pairs with Given Sum | Nested loops | Hash Map |
| Kth Smallest Pair Sum | Generate and sort all sums | Binary Search + Two Pointers |

---

## Files Included

Suggested Python filenames:

- `prime_sum_comparison.py`
- `pair_sum_comparison.py`
- `kth_smallest_pair_sum.py`

---

## How to Run the Programs

1. Clone or download the repository.
2. Open the project folder in Visual Studio Code.
3. Navigate to the required Python file.
4. Open the integrated terminal.
5. Execute the program using:

       python filename.py

6. Observe the output and execution time.

---

## Learning Outcomes

After completing these programs, the following concepts are understood:

- Difference between naive and optimized algorithms.
- Understanding time and space complexity.
- Application of Big-O notation.
- Prime number generation techniques.
- Sieve of Eratosthenes.
- Hash Maps and dictionary operations.
- Pair counting using nested loops.
- Sorting and binary search.
- Two-pointer technique.
- Performance measurement using Python's `time` module.
- Importance of selecting efficient algorithms for large inputs.

---

## Conclusion

This assignment demonstrates how algorithm optimization can significantly improve program performance.

By comparing naive and optimized approaches, it becomes clear that choosing an appropriate algorithm is essential when working with large datasets.

Techniques such as the Sieve of Eratosthenes, Hash Maps, Binary Search, and Two-Pointer methods help reduce execution time and improve computational efficiency.

---

## Student Details

- **Name:** Aayush Singh
- **Roll Number:** IC-2K24-04
- **Course:** MCA (5 Years)
- **Semester:** 5th Semester
- **Subject:** Python Programming

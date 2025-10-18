# Meta Hacker Cup Solutions 🏆

A comprehensive collection of solutions for Meta (Facebook) Hacker Cup competitive programming challenges across multiple years (2023-2025). This repository showcases problem-solving approaches using Python, covering various algorithmic concepts including dynamic programming, number theory, graph algorithms, and mathematical optimization.

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Solutions by Year](#solutions-by-year)
  - [2023 Practice Round](#2023-practice-round)
  - [2024 Practice Round](#2024-practice-round)
  - [2024 Round 1](#2024-round-1)
  - [2025 Competition](#2025-competition)
- [Key Algorithms & Techniques](#key-algorithms--techniques)
- [Notable Achievements](#notable-achievements)
- [How to Use](#how-to-use)
- [Technologies](#technologies)

## 🎯 Overview

Meta Hacker Cup is an annual worldwide programming competition where participants solve algorithmic problems to advance through multiple rounds. This repository contains my solutions developed during the 2023-2025 competitions, demonstrating various problem-solving strategies and algorithmic implementations.

## 📁 Project Structure

```
Meta Hacker Cup/
├── Meta Hacker Cup 2023 Practice Round/
│   ├── Q1/ - Cheeseburger Corollary Problem
│   └── Q2/ - Practice Problem
├── Meta Hacker Cup 2024 Practice Round/
│   ├── Q1/ - Walk the Line
│   ├── Q2/ - Line by Line
│   ├── Q3/ - Problem C
│   └── Q4/ - Problem D
├── Meta Hacker Cup 2024 Round 1/
│   ├── Prime Subtractorization/
│   ├── Subsonic Subway/
│   ├── Substitution Cipher/
│   └── Problem E Wildcard Submissions/
└── Meta Hacker Cup 2025/
    ├── Crash Course/
    ├── Final Product (Chapter 1)/
    ├── Final Product (Chapter 2)/
    ├── Narrowing Down/
    ├── Snake Scales (Chapter 1)/
    └── Snake Scales (Chapter 2)/
```

Each problem directory typically contains:
- `code.py` or `pro.py` - Solution implementation
- `input.txt` - Test input data
- `output.txt` - Generated output
- Additional test files and validation inputs

## 🚀 Solutions by Year

### 2023 Practice Round

#### Q1: Cheeseburger Corollary
**Problem Type:** Logic/Comparison  
**Difficulty:** Easy

**Problem Description:**  
A simple comparison problem involving parameters R (rows), C (columns), A and B. Determines whether specific conditions are met based on grid dimensions.

**Approach:**
- Simple conditional check comparing R and C values
- Direct comparison logic: returns "Yes" if R > C, else "No"

**Key Concepts:**
- Basic input/output handling
- Conditional logic

**Files:** `Q1/pro.py`

---

#### Q2: Practice Problem
**Status:** Solution file present but implementation details minimal

---

### 2024 Practice Round

#### Q1: Walk the Line
**Problem Type:** Optimization/Greedy Algorithm  
**Difficulty:** Easy-Medium

**Problem Description:**  
Given N people with different crossing speeds S[i] and a time limit K, determine if all people can cross within the time constraint using optimal strategy.

**Approach:**
- Sort crossing times for optimal arrangement
- Calculate total time using greedy strategy: fastest person escorts others back
- Formula: `2 * S[0] * (N - 2) + S[0]` for N ≥ 2
- Compare against time limit K

**Key Concepts:**
- Greedy algorithms
- Sorting and optimization
- Bridge crossing problem variant

**Time Complexity:** O(N log N) due to sorting

**Files:** `Q1/pro3.py`

---

#### Q2: Line by Line
**Problem Type:** Probability/Mathematics  
**Difficulty:** Medium

**Problem Description:**  
Calculate the probability adjustment needed when N people work on a project instead of 1, where the success probability changes.

**Approach:**
- Mathematical formula: `P_new = (P/100)^((N-1)/N) * 100`
- Calculate the increase from original probability P
- High precision output (15 decimal places)

**Key Concepts:**
- Probability theory
- Exponential calculations
- Floating-point precision

**Files:** `Q2/pro.py`

---

### 2024 Round 1

*🏅 Successfully completed Round 1 - Certificate earned!*

#### Prime Subtractorization
**Problem Type:** Number Theory  
**Difficulty:** Medium-Hard

**Problem Description:**  
Find the number of unique prime differences ("subtractorizations") that can be formed from primes ≤ N. A subtractorization occurs when the difference of two primes is also prime.

**Approach:**
- Generate primes using Sieve of Eratosthenes up to N²
- For each pair of primes p1, p2 ≤ N, check if |p2 - p1| is prime
- Store unique prime differences in a set
- Count total unique subtractorizations

**Key Concepts:**
- Sieve of Eratosthenes
- Prime number generation
- Set operations for uniqueness
- Number theory

**Time Complexity:** O(N² log log N) for sieve + O(P²) for pair checking where P is number of primes

**Files:** `Prime Subtractorization/pro.py`

---

#### Subsonic Subway
**Problem Type:** Binary Search/Optimization  
**Difficulty:** Medium

**Problem Description:**  
Find the minimum constant speed for a subway to deliver packages to N stations, where each station i has a time window [A_i, B_i] during which delivery is valid.

**Approach:**
- Calculate speed bounds for each station:
  - Lower bound: `max(distance_i / B_i)` (must arrive by deadline)
  - Upper bound: `min(distance_i / A_i)` (can't arrive too early)
- Track global lower and upper bounds
- If bounds cross (lower > upper), return -1 (impossible)
- Otherwise return minimum valid speed (lower bound)

**Key Concepts:**
- Constraint satisfaction
- Range intersection
- Physics (speed = distance/time)
- Feasibility checking

**Time Complexity:** O(N)

**Files:** `Subsonic Subway/pro.py`

---

#### Substitution Cipher
**Problem Type:** Dynamic Programming/String Processing  
**Difficulty:** Hard

**Problem Description:**  
Given an encoded string with '?' wildcards and K, find the K-th lexicographically smallest string that maximizes the number of valid decodings (where digits map to letters A-Z).

**Approach:**
1. Generate all possible strings by replacing '?' with digits 0-9
2. For each string, count decodings using DP:
   - `dp[i]` = number of ways to decode string up to position i
   - Consider single digit (1-9) and two-digit (10-26) decodings
3. Find maximum decoding count
4. Sort strings with max count lexicographically
5. Return K-th string and count % 998244353

**Key Concepts:**
- Dynamic programming
- String manipulation
- Backtracking/enumeration
- Lexicographic sorting
- Modular arithmetic

**Time Complexity:** O(10^Q * N) where Q is number of '?' and N is string length

**Files:** `Substitution Cipher/pro.py`

---

### 2025 Competition

#### Crash Course
**Problem Type:** Array Processing/XOR Properties  
**Difficulty:** Medium

**Problem Description:**  
Calculate the minimum cost to "flatten" all contiguous subarrays of size N to all zeros, where cost depends on XOR properties and segment structure.

**Approach:**
- For each subarray, calculate flattening cost:
  - All zeros: cost = 0
  - Single non-zero element: cost = 1
  - XOR ≠ 0: impossible, cost = length
  - XOR = 0: cost based on segments and transitions
- Count contiguous segments and transitions between different values
- Sum costs across all subarrays

**Key Concepts:**
- XOR properties
- Subarray processing
- Segment counting
- Bitwise operations

**Time Complexity:** O(N³) for all subarrays and their analysis

**Files:** `Crash Course/code.py`

---

#### Final Product (Chapter 1)
**Problem Type:** Number Theory/Combinatorics  
**Difficulty:** Medium

**Problem Description:**  
Find a sequence of 2N multipliers where coolness starts at 1, reaches ≤A after N days, and equals B after 2N days. Construct one valid sequence.

**Approach:**
1. Find largest divisor of B that is ≤ A (intermediate value)
2. First N days: use (N-1) multipliers of 1, then multiply by intermediate
3. Next N days: use (N-1) multipliers of 1, then multiply by (B/intermediate)
4. This ensures constraints are met

**Key Concepts:**
- Divisor finding
- Greedy construction
- Number factorization

**Time Complexity:** O(√B) for divisor search

**Files:** `Final Product (Chapter 1)/code.py`

---

#### Final Product (Chapter 2)
**Problem Type:** Dynamic Programming/Combinatorics  
**Difficulty:** Hard

**Problem Description:**  
Count the number of valid sequences of 2N multipliers satisfying the Final Product constraints. Result modulo 10⁹ + 7.

**Approach:**
1. Find all divisors of B that are ≤ A (valid intermediate values)
2. For each valid intermediate value:
   - Count factorizations from 1 to intermediate in N steps
   - Count factorizations from intermediate to B in N steps
   - Multiply counts for this path
3. Use memoized DP to count ordered factorizations
4. Sum all valid paths modulo 10⁹ + 7

**Key Concepts:**
- Dynamic programming with memoization
- Counting ordered factorizations
- Modular arithmetic
- Divisor enumeration
- Combinatorial counting

**Time Complexity:** O(D * N * √B) where D is number of divisors

**Files:** `Final Product (Chapter 2)/code.py`, `another.py`, `app.py`

---

#### Narrowing Down
**Problem Type:** Algorithm Analysis/Debugging  
**Difficulty:** Hard

**Problem Description:**  
Complex problem requiring extensive testing and algorithm refinement, as evidenced by multiple test files.

**Approach:**
- Multiple iterations and test cases
- Deep analysis of edge cases
- Pattern recognition and algorithm optimization

**Key Files:**
- `code.py` - Main solution
- `deep_analysis.py` - Detailed analysis approach
- Multiple test files for edge cases, patterns, and specific scenarios

**Files:** Multiple test scripts demonstrating thorough testing methodology

---

#### Snake Scales (Chapter 1)
**Problem Type:** Array/Simple Math  
**Difficulty:** Easy

**Problem Description:**  
Given N platform heights, find the minimum ladder size needed to traverse between consecutive platforms.

**Approach:**
- Special case: single platform needs no ladder (return 0)
- Calculate absolute difference between each pair of consecutive platforms
- Return maximum difference as minimum required ladder size

**Key Concepts:**
- Array traversal
- Maximum finding
- Edge case handling

**Time Complexity:** O(N)

**Files:** `Snake Scales (Chapter 1)/code.py`

---

#### Snake Scales (Chapter 2)
**Problem Type:** Advanced variant  
**Difficulty:** Medium-Hard

Extended version of Snake Scales with additional constraints and complexity.

**Files:** `Snake Scales (Chapter 2)/code.py`

---

## 🧠 Key Algorithms & Techniques

Throughout these solutions, the following algorithmic concepts are demonstrated:

### Mathematical & Number Theory
- **Sieve of Eratosthenes** - Efficient prime generation
- **Divisor Finding** - Integer factorization
- **Modular Arithmetic** - Large number handling (mod 10⁹+7, 998244353)
- **Probability Calculations** - Expected value and exponential probability

### Dynamic Programming
- **String Decoding DP** - Counting valid interpretations
- **Factorization Counting** - Ordered factor enumeration
- **Memoization** - Optimization for recursive solutions

### Greedy Algorithms
- **Optimization Problems** - Bridge crossing, resource allocation
- **Sorting Strategies** - Optimal ordering for time/cost minimization

### Data Structures
- **Sets** - Uniqueness tracking
- **Arrays/Lists** - Efficient data access
- **Hash Tables (Dictionaries)** - Memoization and caching

### Other Techniques
- **Constraint Satisfaction** - Bound checking and feasibility
- **XOR Properties** - Bitwise manipulation
- **Segment Analysis** - Contiguous region processing
- **Binary Search** - Optimization in constrained spaces

## 🏅 Notable Achievements

- ✅ **Completed 2024 Round 1** - Earned official certificate
- 🎯 **Solved 15+ unique problems** across multiple difficulty levels
- 💡 **Implemented advanced algorithms** including DP, number theory, and optimization
- 📊 **Comprehensive testing** with validation inputs and edge cases

## 🔧 How to Use

### Running Solutions

Each solution is self-contained and follows a consistent structure:

```bash
# Navigate to problem directory
cd "Meta Hacker Cup 2024 Round 1/Prime Subtractorization"

# Run the solution
python pro.py

# Or with explicit input/output
python pro.py < input.txt > output.txt
```

### Input/Output Format

Most solutions follow the standard Hacker Cup format:
```
First line: T (number of test cases)
Next T blocks: Test case data
Output: Case #X: [result]
```

### Testing

Solutions are tested against:
- Sample inputs provided by Meta
- Validation inputs (when available)
- Custom edge cases

## 💻 Technologies

- **Language:** Python 3.x
- **Key Libraries:** 
  - Standard library (no external dependencies in most solutions)
  - Built-in math, itertools for combinatorics
- **Paradigms:**
  - Functional programming
  - Dynamic programming
  - Greedy algorithms
  - Mathematical optimization

## 📈 Problem Difficulty Distribution

| Year | Round | Easy | Medium | Hard |
|------|-------|------|--------|------|
| 2023 | Practice | 2 | 0 | 0 |
| 2024 | Practice | 2 | 2 | 0 |
| 2024 | Round 1 | 0 | 3 | 1 |
| 2025 | Competition | 2 | 3 | 1 |

## 🎓 Learning Outcomes

This repository demonstrates proficiency in:

1. **Algorithm Design** - Creating efficient solutions for complex problems
2. **Code Optimization** - Writing performant code within time constraints
3. **Problem Decomposition** - Breaking down complex problems into manageable parts
4. **Testing & Validation** - Ensuring correctness across various test cases
5. **Mathematical Reasoning** - Applying number theory, probability, and combinatorics
6. **Competitive Programming** - Rapid problem-solving under competition conditions

## 📝 Notes

- Solutions prioritize correctness and clarity
- Time complexity is crucial for passing large test cases
- Most solutions use Python's built-in capabilities for efficiency
- Comments in code explain key algorithmic decisions

## 🔗 Related Links

- [Meta Hacker Cup Official Site](https://www.facebook.com/codingcompetitions/hacker-cup)
- [Competition Archive](https://www.facebook.com/codingcompetitions/hacker-cup/past-editions)

---

**Author:** Competitive Programming Enthusiast  
**Last Updated:** 2025  
**Status:** Active - Continuously updating with new solutions

*"The only way to learn a new programming language is by writing programs in it." - Dennis Ritchie*


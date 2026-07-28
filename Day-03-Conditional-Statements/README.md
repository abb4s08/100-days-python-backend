# Day 03 - Python Conditional Statements and Decision Making

## 📚 Topics Covered

- Conditional statements
- `if` statement
- `if-else` statement
- `if-elif-else` statement
- Nested `if` statements
- Comparison operators
- Logical operators
- Combining multiple conditions
- `match-case`
- Decision-making in Python

---

## 💻 Practice Problems

### 1. Leap Year Checker

Write a Python program that takes a year as input and determines whether it is a leap year.

A year is a leap year if:

- It is divisible by 400, OR
- It is divisible by 4 but not divisible by 100

Otherwise, it is not a leap year.

**Sample Input**
```text
2024
```

**Sample Output**
```text
Leap Year
```

**Example 2**

**Sample Input**
```text
1900
```

**Sample Output**
```text
Not a Leap Year
```

---

### 2. Grade Classifier

Write a Python program that takes a student's mark as input and displays the corresponding grade.

Use the following grading system:

| Marks | Grade |
|---|---|
| 90 - 100 | A |
| 80 - 89 | B |
| 70 - 79 | C |
| 60 - 69 | D |
| Below 60 | F |

**Sample Input**
```text
85
```

**Sample Output**
```text
Grade: B
```

**Example 2**

**Sample Input**
```text
95
```

**Sample Output**
```text
Grade: A
```

---

### 3. Largest of Three Numbers

Write a Python program that takes three numbers as input and determines the largest number using conditional statements.

Do not use the built-in `max()` function.

**Sample Input**
```text
10
25
15
```

**Sample Output**
```text
Largest: 25
```

**Example 2**

**Sample Input**
```text
50
20
80
```

**Sample Output**
```text
Largest: 80
```

---

### 4. Triangle Type

Write a Python program that takes the lengths of three sides of a triangle as input.

First, determine whether the three sides can form a valid triangle.

A triangle is valid when:

```text
a + b > c
a + c > b
b + c > a
```

If the triangle is valid, classify it as:

- **Equilateral** - All three sides are equal
- **Isosceles** - Any two sides are equal
- **Scalene** - All three sides are different

**Sample Input**
```text
5
5
5
```

**Sample Output**
```text
Equilateral Triangle
```

**Example 2**

**Sample Input**
```text
5
5
8
```

**Sample Output**
```text
Isosceles Triangle
```

**Example 3**

**Sample Input**
```text
3
4
5
```

**Sample Output**
```text
Scalene Triangle
```

**Example 4**

**Sample Input**
```text
1
2
5
```

**Sample Output**
```text
Invalid Triangle
```

---

### 5. Pricing Logic

Write a Python program that takes the total purchase amount as input and calculates a discount based on the following rules:

| Purchase Amount | Discount |
|---|---:|
| ₹5,000 or more | 20% |
| ₹3,000 - ₹4,999 | 15% |
| ₹1,000 - ₹2,999 | 10% |
| Below ₹1,000 | No discount |

Display:

- Original amount
- Discount amount
- Final amount after discount

**Sample Input**
```text
4000
```

**Sample Output**
```text
Original Amount: ₹4000.00
Discount: ₹600.00
Final Amount: ₹3400.00
```

**Example 2**

**Sample Input**
```text
800
```

**Sample Output**
```text
Original Amount: ₹800.00
Discount: ₹0.00
Final Amount: ₹800.00
```

---

## 🚀 Daily Project - Decision Engine

Build a **Decision Engine** that allows the user to select and execute different decision-making programs.

The program should display the following menu:

```text
===== Decision Engine =====

1. Leap Year Checker
2. Grade Classifier
3. Largest of Three Numbers
4. Triangle Type Checker
5. Pricing Calculator
6. Exit
```

Take the user's choice as input and perform the corresponding operation.

Use:

- `if`
- `elif`
- `else`
- Nested conditions
- Logical operators
- `match-case`

### Sample Input

```text
===== Decision Engine =====

1. Leap Year Checker
2. Grade Classifier
3. Largest of Three Numbers
4. Triangle Type Checker
5. Pricing Calculator
6. Exit

Enter your choice: 1

Enter year: 2024
```

### Sample Output

```text
2024 is a Leap Year
```

### Another Example

**Sample Input**
```text
Enter your choice: 3

Enter number 1: 15
Enter number 2: 40
Enter number 3: 25
```

**Sample Output**
```text
Largest: 40
```

---

## 🛠️ Skills Practiced

Through these problems, I practiced:

- Writing `if` statements
- Using `if-else`
- Creating multiple conditions using `if-elif-else`
- Writing nested conditional statements
- Using comparison operators
- Combining conditions using `and`, `or`, and `not`
- Using `match-case`
- Validating conditions before processing data
- Implementing real-world decision-making logic
- Breaking problems into multiple conditions

---

## 📁 Files

- `01_leap_year.py`
- `02_grade_classifier.py`
- `03_largest_of_three.py`
- `04_triangle_type.py`
- `05_pricing_logic.py`
- `06_project_decision_engine.py`

---

## 🎯 Day 03 Goal

By the end of Day 03, I should be able to:

- Understand how programs make decisions
- Use `if`, `elif`, and `else` correctly
- Write nested conditional statements
- Combine multiple Boolean conditions
- Use `match-case` for structured choices
- Solve decision-making problems independently

---

## 🚀 100 Days of Python Backend Development

**Day 03 Complete ✅**

Building stronger Python problem-solving skills one day at a time.
#  **Day 2 – Data Types, Math, and Tip Calculator (with Examples)**

## **Python Primitive Data Types**

**What I learned:**
Python has 4 main primitive data types.

**Examples:**

```python
# Integer
age = 21

# Float
price = 19.99

# String
name = "TJ"

# Boolean
is_coding = True
```

---

## **Type Checking**

**What I learned:**
Use `type()` to check the data type of a value or variable.

**Example:**

```python
print(type(21))        # <class 'int'>
print(type("Hello"))   # <class 'str'>
```

---

## **Type Conversion (Fixing TypeErrors)**

**What I learned:**
Convert string → number when doing math.

**Example:**

```python
num = "5"
total = int(num) + 10
print(total)  # 15
```

---

## **Mathematical Operations**

**What I learned:**
Python supports several math operators.

**Examples:**

```python
3 + 2   # Addition
5 - 1   # Subtraction
4 * 3   # Multiplication
10 / 3  # Division (float)
10 // 3 # Floor division
10 % 3  # Remainder
2 ** 3  # Power
```

---

## **BMI Calculator (exercise)**

**What I learned:**
Convert input, do simple math, output result.

**Example:**

```python
height = float(input("Height (m): "))
weight = float(input("Weight (kg): "))

bmi = weight / (height ** 2)
print(int(bmi))
```

---

## **Number Manipulation + Rounding**

**What I learned:**
Use `round()` to clean up messy decimal results.

**Example:**

```python
result = 3.14159
print(round(result, 2))  # 3.14
```

---

## **F-Strings**

**What I learned:**
Insert variables into strings without messy concatenation.

**Example:**

```python
name = "TJ"
score = 98
print(f"{name} scored {score} on the test!")
```

---

## **Day 2 Project: Tip Calculator**

**What I learned:**
Take inputs → convert → do math → use f-string → print result.

**Example:**

```python
bill = float(input("Bill amount: "))
tip = int(input("Tip %: "))
people = int(input("Number of people: "))

tip_amount = bill * (tip / 100)
total_bill = bill + tip_amount
result = total_bill / people

print(f"Each person should pay: ${round(result, 2)}")
```

---

## **Wins**

* Understood the difference between strings and numbers
* Fixed TypeErrors with conversions
* Used math operators confidently
* Started writing cleaner output with f-strings

---

## **Next Steps**

* Learn conditionals and branching logic (if/else)
* Build the Day 3 project

---


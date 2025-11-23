
# Day 3 – Conditionals, Logical Operators, Nesting & Modulo

## Comparator Operators
```

> Greater than
> <   Less than
> =  Greater than or equal
> <=  Less than or equal
> ==  Equal to
> !=  Not equal

````

## Logical Operators
```python
A and B     # both conditions must be true
A or B      # at least one must be true
not A       # true when A is false
````

Example:

```python
age = 50
if age >= 45 and age <= 55:
    print("Free ride")
```

## If / Elif / Else

```python
if condition:
    do_a()
elif other_condition:
    do_b()
else:
    do_c()
```

Only one block is executed.

## Nested If Statements

```python
if cond1:
    if cond2:
        if cond3:
            do_something()
```

All conditions must be true.

## Multiple Independent If Statements

```python
if cond1:
    do_a()
if cond2:
    do_b()
if cond3:
    do_c()
```

Each condition runs independently.

## Modulo Operator (%)

Returns the remainder.

```python
6 % 2   # 0
6 % 5   # 1
6 % 4   # 2
10 % 3  # 1
```

### Odd or Even Check

```python
num = int(input("Number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## Example Project: Python Pizza Calculator

```python
print("Welcome to Python Pizza Deliveries!")

size = input("S, M or L: ")
pepperoni = input("Pepperoni? Y or N: ")
extra_cheese = input("Extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
```

## Indentation Rules

* Lines inside an if-block must be indented
* Parent line → child block

Example:

```python
if 5 > 2:
    print("Yes")
```

## What I Learned Today

* Comparison operators
* Logical operators (and, or, not)
* If/elif/else
* Nested if statements
* Multiple independent if statements
* Modulo operator
* Odd/even logic
* Importance of indentation
* Building logic-based scripts (Pizza calculator + adventure game)

```
BuiltByVision

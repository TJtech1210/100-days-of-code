Day 3 – Conditionals, Logical Operators, Nesting, and Modulo
Comparator Operators
>   Greater than  
<   Less than  
>=  Greater than or equal to  
<=  Less than or equal to  
==  Equal to  
!=  Not equal to

Logical Operators
A and B     # both conditions must be true
A or B      # at least one condition must be true
not A       # true if A is false


Example:

age = 50
if age >= 45 and age <= 55:
    print("Free ride")

If / Elif / Else

Only one block runs in this structure.

if condition:
    do_a()
elif other_condition:
    do_b()
else:
    do_c()

Nested If Statements

Conditions inside conditions. All must be true to reach the innermost code.

if cond1:
    if cond2:
        if cond3:
            do_something()

Multiple Independent If Statements

All conditions are checked, regardless of each other.

if cond1:
    do_a()
if cond2:
    do_b()
if cond3:
    do_c()

Modulo Operator (%)

Returns the remainder of a division.

6 % 2   # 0
6 % 5   # 1
6 % 4   # 2
10 % 3  # 1

Odd or Even Check
num = int(input("Number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

Example Project: Python Pizza Calculator
print("Welcome to Python Pizza Deliveries!")

size = input("S, M or L: ")
pepperoni = input("Pepperoni? Y or N: ")
cheese = input("Extra cheese? Y or N: ")

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

if cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")

Indentation Rules

Lines inside an if-block must be indented

Parent line → child block

Example:

if 5 > 2:
    print("Yes")

What I Learned Today

Comparison operators

Logical operators (and, or, not)

If/elif/else structure

Nested if statements

Multiple independent if statements

Modulo operator and odd/even logic

Importance of indentation

Building logic-based scripts (Pizza calculator + adventure game)

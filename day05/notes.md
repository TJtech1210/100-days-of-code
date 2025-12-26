# Day 5 – For Loops and Password Generator

## What I Learned Today

### For Loops
- Looping over a range: `for i in range(5):`
- Looping through lists: `for item in list:`
- Using loops to repeat actions dynamically based on user input.

### Randomisation Review
- Using `random.choice(list)` to select random items.
- Using `random.shuffle(list)` to randomize order.

### Password Generator Logic
- Building a password by appending random letters, numbers, and symbols.
- Storing characters in a list before shuffling.
- Converting a list into a final string using `"".join()` or a loop.
- Understanding how to avoid predictable patterns by shuffling.

### Clean Code Practices
- Keeping character sets organized (letters, numbers, symbols).
- Structuring the script top-down (input → generation → shuffle → output).
- Using lists instead of direct string concatenation for performance.

---

## Day 5 Project
See `password_generator.py` in this folder.

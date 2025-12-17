import random

# ASCII Art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# User Input
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

# Input Validation
if user_input < 0 or user_input > 2:
    print("Invalid choice.")
    exit()

# Game Setup
options = [rock, paper, scissors]
computer_input = random.randint(0, 2)

# Show Results
print("\nYou chose:")
print(options[user_input])

print(f"Computer chose ({computer_input}):")
print(options[computer_input])

# Game Logic
if user_input == computer_input:
    print("It's a Tie!")
elif user_input == 1 and computer_input == 0:
    print("You Win!")
elif user_input == 0 and computer_input == 2:
    print("You Win!")
elif user_input == 2 and computer_input == 1:
    print("You Win!")
else:
    print("Computer Wins!")

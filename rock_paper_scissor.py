import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

ROCK
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

PAPER
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

SCISSOR
'''

game_images = [rock, paper, scissors]

while True:
    # Ask the user for their choice
    user_input = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. Type 'quit' to exit.\n")
    
    # Check if the user wants to quit
    if user_input.lower() == "quit":
        print("Thanks for playing! Goodbye!")
        break

    # Convert user input to an integer if possible
    try:
        user_choice = int(user_input)
    except ValueError:
        print("Invalid input. Please enter 0, 1, 2, or 'quit' to exit.")
        print("-" * 30)  # Line separator after invalid input
        continue

    # Validate the user's choice
    if user_choice < 0 or user_choice > 2:
        print("You typed an invalid number. You lost this round!")
        print("-" * 30)  # Line separator after invalid choice
        continue

    # Print the user's choice
    print("You chose:")
    print(game_images[user_choice])

    # Generate the computer's choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # Determine the outcome
    if user_choice == 0 and computer_choice == 2:
        print("You won this round!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lost this round!")
    elif computer_choice > user_choice:
        print("You lost this round!")
    elif user_choice > computer_choice:
        print("You won this round!")
    else:
        print("It's a draw!")
    
    # Line separator for clarity at the end of each round
    print("-" * 100)

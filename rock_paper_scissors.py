import random
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
print("Welcome to the Rock Paper Scissors game!")
play = True
game_choices = [rock, paper, scissors]
while play:
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    computer_choice = random.randint(0,2)
    print(game_choices[player_choice])
    print("Computer chose: ", game_choices[computer_choice])
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 0):
        print("You lose.")
    else:
        print("You win!")
    again = input("Type 'y' to play again or 'q' to quit\n")
    if again != "y":
        print("Thanks for playing!")
        play = False
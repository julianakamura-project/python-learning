import random

print("Welcome to the Banker Roulette!\n")
participants = []
num_players = int(input("How people will be participating? \n"))
print("Please input the names of the players.\n")
for i in range(num_players):
    participants.append(input(f"Player {i+1}: "))
print("")
play = True
while play:
    roulette = random.randint(0,len(participants)-1)
    print(f"The one paying will be {participants[roulette]}!\n")
    again = input("Would you like to play again? (y/n)\n")
    if again != "y":
        print("Thank you for playing!")
        play = False
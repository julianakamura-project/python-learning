import random
input("Welcome to the coin flipper!\nPress Enter to flip a coin.\n")
play = True
while play:
    rand_num = random.randint(0, 1)
    if rand_num == 0:
        print("Heads!\n")
    else:
        print("Tails!\n")
    continue_play = input("Would you like to flip another coin? (y/n)\n")
    if continue_play == "n":
        print("Goodbye!")
        play = False
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
#First Room, Left or Right
left_or_right = input("Which way would you like to go? Left or Right? ")
if left_or_right != "Left":
    print("You fall into a hole.\nGame Over.")
else:
    swim_or_wait = input("You reach a building surrounded by a river.\nThe bridge to cross over is raised.\nDo you Swim or Wait? ")
    if swim_or_wait != "Wait":
        print("You are attacked by trouts.\nGame Over.")
    else:
        which_door = input("Your patience proves true and the bridge is lowered.\nThe building has three doors: Red, Yellow and Blue.\nWhich door do you enter? ")
        if which_door == "Red":
            print("The door closes behind you.\nThe room lits up in flames.\nGame Over.")
        elif which_door == "Blue":
            print("The door closes behind you.\nBeasts jump at you.\nGame Over.")
        elif which_door == "Yellow":
            print("The door opens to reveal the Treasure Room!\nCongratulations, you win!")
        else:
            print("You don't know which door to choose.\nYou turn around and leave.\nGame Over.")
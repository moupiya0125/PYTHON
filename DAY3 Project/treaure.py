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

# Get user inputs and convert to lowercase for consistent comparison
direction = input("You've arrived at a road division. Which way do you want to go? Type 'left' or 'right': ").lower()

if direction == "left":
    print("Yayyy, you chose the right way. Please go on.")
    river = input("You've arrived at the river... Do you want to swim or wait for the boat? Type 'swim' or 'wait': ").lower()
    if river == "wait":
        print("Yayyy, the boat arrived and you crossed the river successfully.")
        door = input("You've arrived at the Treasure Palace. Which door do you choose? Red, Blue, or Yellow? ").lower()
        if door == "blue":
            print("There were beasts in this room. Game over.")
        elif door == "red":
            print("Burned by fire. Game Over.")
        elif door == "yellow":
            print("You win! You found the treasure! 🎉")
        else:
            print("That door doesn't exist. Game Over.")
    else:
        print("Oops! You were attacked by a trout. Game over.")
elif direction == "right":
    print("Oops! You fell in a hole. Game over.")
else:
    print("Invalid direction. Game over.")

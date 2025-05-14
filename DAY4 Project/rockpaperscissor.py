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
option_list = [rock,paper,scissors]
My_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

Computer_choice = random.randint(0,2)

if My_choice == 0 and Computer_choice == 1:
    print(f"You chose : {option_list[0]}")
    print(f"Computer chose: {option_list[1]}")
    print("COMPUTER WIN")

elif My_choice == 0 and Computer_choice == 2:
    print(f"You chose : {option_list[0]}")
    print(f"Computer chose:{option_list[2]}")
    print("YOU WIN")

elif My_choice == 1 and Computer_choice == 0:
    print(f"You chose : {option_list[1]}")
    print(f"Computer chose:{option_list[0]}")
    print("YOU WIN")

elif My_choice == 1 and Computer_choice == 2:
    print(f"You chose : {option_list[1]}")
    print(f"Computer chose:{option_list[2]}")
    print("COMPUTER WIN")

elif My_choice == 2 and Computer_choice == 0:
    print(f"You chose : {option_list[2]}")
    print(f"Computer chose:{option_list[0]}")
    print("COMPUTER WIN")

elif My_choice == 2 and Computer_choice == 1:
    print(f"You chose : {option_list[2]}")
    print(f"Computer chose:{option_list[1]}")
    print("YOU WIN")

elif My_choice == Computer_choice:
    print(f"You chose:{option_list[My_choice]} ")
    print(f"Computer chose:{option_list[Computer_choice]}")
    print("IT IS A DRAW")

else:
    print("WRONG INPUT")
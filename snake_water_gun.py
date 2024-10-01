import random
import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

'''
1 for snake
-1 for water
0 for gun
'''
clear_console()
print("\n", "*" * 48)
print(" " * 10, "SNAKE, WATER, AND GUN GAME", " " * 10)
print("", "*" * 48, "\n")
print("\n\tRULE: To win this game, you have to score 5 points before the computer.\n")
p_name = input("\nEnter your name: ")


loose = 0
wins = 0

while(True):

    computer = random.choice([-1, 0, 1])

    print("\nGet ready...")
    for i in range(3, 0, -1):
        print(i, "...")
        time.sleep(1)

    clear_console()
    print("""
Choose s for Snake🐍
Choose w for Water💦
Choose g for Gun🔫
          """)
    youstr = input("Enter your move: ")

    youDict = {"s": 1, "w": -1, "g": 0}
    reverseDict = {1: "Snake🐍", -1: "Water💦", 0: "Gun🔫"}

    you = youDict.get(youstr)
    if you is None:  # Handle invalid input
        print("Invalid input! Please choose 's', 'w', or 'g'. 😶‍🌫️\n")
        continue

    print(f"You chose {reverseDict.get(you)}\nComputer chose {reverseDict[computer]}")

    if(computer == you):
        print("It's a draw!📍")

    else:
        if (you == 1 and computer == -1) or (you == 0 and computer == 1) or (you == -1 and computer == 0):
            print("You win!🎉")
            wins += 1
        else:
            print("You lose!🫠")
            loose += 1

        print(f"\nCurrent Score: {p_name}: {wins} | Computer: {loose}\n")


        if(wins == 5 or loose == 5):
            break


if wins > loose:
    print(f"Congratulations {p_name}! You Won 🏆🎊")
else:
    print(f"Sorry {p_name}, but you loose! Better luck next time👍")

print("\n", "*" * 10, "THANK YOU FOR PLAYING!", "*" * 10, "\n")

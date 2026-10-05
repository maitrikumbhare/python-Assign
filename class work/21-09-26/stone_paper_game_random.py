# stone, paper, scissors game using list with random library
import random

lucky = ["stone", "paper", "scissors"]

random_choice = random.choice(lucky)


while True:
    print("*******Enter your choice*******")
    choice = input("enter your choice: ")
    print("Opponent's choice is:", random_choice)

    if choice not in lucky:
        print("Invalid choice!!")
        break
    elif choice==random_choice:
        print("match draw!!")
        break
    elif random_choice=="stone" and choice=="scissors":
        print("you lose!!")
        break
    elif random_choice=="scissors" and choice=="paper":
        print("you lose!!")
        break
    else:
        print("you win!!")
        break

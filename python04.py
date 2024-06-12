# Guess the number game
import random
r1 = random.randint(1, 100)

while True:
    print("Guess the correct number to win or type Q to quit")
    user_input = input("Guess the number:")
    if user_input == "Q":
        break
    if r1 == int(user_input):
        print("You have the correct guess.\nCongratulations....")
        break
    elif int(user_input) > r1:
        print("The number is higher than the actual number")
    elif int(user_input) < r1:
        print("The number is lower than the actual number")
print("-----GAME OVER-----")

import random
import game_img

game_list = [game_img.rock, game_img.paper, game_img.scissors]

user = int(input("What do you choose? Type 1 for Rock, 2 for Paper, or 3 for Scissors.\n")) - 1
computer = random.randint(0, 2)

if user > 2 or user < 0:
	print("You typed an invalid number, YOU LOSE!!!")
else:
	print(game_list[user])
	print(f"Computer chose:\n{game_list[computer]}")

	if computer == user:
		print("DRAW!!")
	elif (computer == 1 and user == 0) or (computer == 2 and user == 1) or (computer == 0 and user == 2):
		print("You lose")
	else:
		print("You win")
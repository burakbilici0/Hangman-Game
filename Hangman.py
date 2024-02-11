import random

def chose_random_word():
	word_bank = ["algorithm", "binary", "compiler", "debugging", "encryption", "firewall", "hardware", "interface", "javascript", "keyboard", "programming", "software", "virtualization", "wifi", "windows"]
	return random.choice(word_bank)

name = input("Please Enter Name: ")
print("Welcome, " + name + " time to play hangman :) ")

secret_word = chose_random_word()
player_guess = ""
lives = 10

while lives > 0:

	player_change = 0

	for x in secret_word:

		if x in player_guess:
			print(x, end=" ")
		else: 
			print("*", end=" ")
			player_change += 1
	print()

	if player_change == 0:
		print("Congratulations! You WON!! :)) ")
		break


	guess = input("Guess a letter: ")

	if guess in player_guess:
		print("You already guessed that letter. Try again.")
		continue

	player_guess += guess

	if guess not in secret_word:
		lives -= 1
		print ("Wrong guess!")
		print(f"You have {lives} left :( ")
		if lives == 0 :
			print("You died! Sorry, you ran out of lives. Game over :( ")


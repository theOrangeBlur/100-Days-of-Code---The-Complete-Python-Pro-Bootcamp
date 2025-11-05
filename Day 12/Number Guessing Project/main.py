import random
from art import logo

HARD_ATTEMPT_NUM = 5
EASY_ATTEMPT_NUM = 10
UPPER_RANGE = 100
print(logo)

#get difficulty from user
difficulty = input("Okay, so you're trying to guess a number 0 to 100. Do you want to play on 'easy' or 'hard'?:\t").lower()
while difficulty != 'easy' and difficulty != 'hard':
    difficulty = input("'easy' or 'hard'?:\t").lower()

#define attempts from difficulty
attempts = EASY_ATTEMPT_NUM
if difficulty == 'hard': attempts = HARD_ATTEMPT_NUM

#play the game
secret_num = random.randint(0,UPPER_RANGE)
user_guess = UPPER_RANGE + 1
for i in range(attempts, 0, -1):
    user_guess = int(input(f"You have {i} guesses remaining. What's your guess?:\t"))
    if user_guess == secret_num:
        print(f"You win!! {user_guess} was correct!")
        exit()
    if user_guess < secret_num:
        print("You're too low.")
    else:
        print("You're too high.")
print(f"Out of guesses, you LOSE! The number was {secret_num}")

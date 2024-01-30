#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)
chosen_difficulty = input("Do you want to play on 'easy or 'hard' difficulty? ")
total_guesses = 0
if chosen_difficulty == 'easy':
  print("EASY: 10 guesses")
  total_guesses = 10
else:
  print("HARD: 5 guesses")
  total_guesses = 5
remaining_guesses = total_guesses

is_game_over = False
target = random.randint(1, 100)
print("\nGuess the number! It's between 1 and 100.")
while not is_game_over:
  print(f"Remaining guesses: {remaining_guesses}")
  guess = int(input("Your guess: "))
  remaining_guesses -= 1
  if guess == target:
    print(f"You guessed it after only {total_guesses-remaining_guesses} attempts!")
    is_game_over = True
  elif guess > target:
    print("Too high!")
  else: 
    print("Too low!")
  
  if remaining_guesses == 0 and not is_game_over:
    print("Out of guesses!")
    is_game_over = True

print(f"The number was {target}")

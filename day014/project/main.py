from replit import clear
from art import logo, vs
from game_data import data
import random


def choose_next_account(compare_to):
  """Returns a random account different from the one passed as parameter"""
  next = random.choice(data)
  while compare_to == next:
    next = random.choice(data)
  return next


def make_guess(first, second):
  """Clear screen, print logo, print score, print description of both accounts and ask player if the second account has more or less followers than the first account"""
  clear()
  print(logo)
  print(f"Your score: {score}")
  print(f"""{first["name"]}, {first["description"]} from {first["country"]}""")
  print(vs)
  print(f"""{second["name"]}, {second["description"]} from {second["country"]}""")
  return input(
    f"""Does {second["name"]} have [M]ore or [L]ess followers than {first["name"]}?\nm/l: """
  )


def is_guess_correct(guess, first, second):
  """If player says more, check that second account has more follwers than first. If player says less, check that second account has less followers than first."""
  if guess == "m":
    return second["follower_count"] > first["follower_count"]
  else:
    return second["follower_count"] < first["follower_count"]



# START
score = -1 # Start at -1 so we can add 1 in the loop and start from 0
second_account = random.choice(data) # In the loop, this will be assigned to first_account
should_continue_playing = True
while should_continue_playing:
  is_game_over = False
  while not is_game_over:
    # If you're here it means you guessed correctly the previous time
    score += 1
    first_account = second_account
    second_account = choose_next_account(first_account)
    guess = make_guess(first_account, second_account)
    is_game_over = not is_guess_correct(guess, first_account, second_account)
  print(f"Game over!\nYour final score: {score}")
  should_continue_playing = input("Play again?\ny/n: ") == "y"
print("Bye!")
from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

bids = {}

is_last_bidder = False
while not is_last_bidder:
    name = input("What's your name? ")
    bid = int(input("How much are you bidding? $"))
    bids[name] = bid
    more_bidders = input("Are there more bidders? yes/no\n")
    is_last_bidder = more_bidders != "yes"
    clear()

highest_bid = -1
winner_name = ""
for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        winner_name = bidder
print(f"The winner is {winner_name} with a bid of ${highest_bid}")

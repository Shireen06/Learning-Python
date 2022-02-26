import os 
os.system('cls')
from art import logo
print(logo)
bidders = {}
bidding_finished = False

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  names = input("What is your name?: ")
  bid = float(input("What is your bid price in $?: "))
  bidders[names] = bid
  should_continue = input("Are there any other bidders? Type 'yes' or 'no': ")
  if should_continue == "no":
    bidding_finished = True
    highest_bidder(bidders)
  elif should_continue == "yes":
    'cls'

"""Secret Bid Program"""
import math
import art

print(art.logo)

bids_placed = {}
continue_bidding = True

while continue_bidding:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: ₦"))

    bids_placed[bidder_name] = bid_amount

    prompt = input("Are there anymore bidders? Type 'yes' or 'no'\n").lower()

    if prompt == 'no':
        continue_bidding = False
    else:
        print("\n" * 1000) # Clear the screen

max_bid = -math.inf
max_bidder = None

for bidder in bids_placed:
    if bids_placed[bidder] > max_bid:
        max_bid = bids_placed[bidder]
        max_bidder = bidder

print(f"The winner is {max_bidder} with a bid of ₦{bids_placed[max_bidder]}")

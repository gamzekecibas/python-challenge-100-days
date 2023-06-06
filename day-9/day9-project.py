## Day 9 - Beginner | Dictionaries & Nesting
## 06.06.2023
## ----
## DAY 9 PROJECT Secret Auction Program
## ----

import os
from day9Utils import logo

os.system('clear')
print(logo)
anotherOffer = "yes"

name = input("What's your name?: ")
bidPrice = int(input("What's your bid?($): "))
bidPrices = {name: bidPrice}

while anotherOffer.lower() == 'yes':
    anotherOffer = input("Are there any other users who want to bid? (yes or no): ")
    if anotherOffer.lower() == 'yes':
        os.system('clear')
        name = input("What's your name?: ")
        bidPrice = int(input("What's your bid?($): "))
        new_bid = {name: bidPrice}
        bidPrices.update(new_bid)

max_bid = max(bidPrices.values())
max_bid_name = list(filter(lambda x: bidPrices[x] == max_bid, bidPrices))[0]
print(f'The highest bid coming from {max_bid_name} with ${max_bid}.')

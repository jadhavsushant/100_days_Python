import os

from art import logo
print(logo)
print("Welcome to the Secret Auction Program !!!")

final_auction_data = {}


def blind_auction(name, amount):
    final_auction_data[name] = amount


is_continue = True
while is_continue:
    user_name = input('What is your Name?:')
    bid_amount = input('Whats your bid?: $')
    blind_auction(name=user_name, amount=bid_amount)
    response = input("Are there any other bidders? Type 'yes' or 'no'.")
    os.system('cls')
    if response == 'no':
        is_continue = False
        bid_owner_name = max(
            zip(final_auction_data.values(), final_auction_data.keys()))[1]
        max_bid_amount = max(final_auction_data.values())
        print(
            f"The winner is {bid_owner_name} with a bid of ${max_bid_amount}.")

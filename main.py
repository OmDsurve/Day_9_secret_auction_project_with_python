from art import logo
print(logo)
def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidders in bidding_record:
        bid_amount = bidding_record[bidders]
        if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner = bidders

    print(f"The winner is {winner} with amount ${highest_bid}")

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name ")
    price = int(input("What is your bid amount $"))
    bids[name]=price
    new_bidding = input("Are there any new bidders? Tyoe yes or no ").lower()
    if new_bidding == "no" :
        continue_bidding = False
        find_highest_bid(bids)
    elif new_bidding == "yes":
        print("\n"*200)

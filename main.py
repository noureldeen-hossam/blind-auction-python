
import art
print(art.logo)
bids = {}
def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")
again = "yes"
while again == "yes":
    name = input("what's your name?\n")
    bid = int(input("what is your bid?\n"))

    bids[name] = bid
    again = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if again == "yes":
        print("\n"*200)
    elif again == "no":
        find_highest_bidder(bids)

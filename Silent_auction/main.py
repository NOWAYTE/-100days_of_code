from art import logo

print(logo)

bids = {}

bidding_finished = False


def finding_highest_bidder(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with the highest bid of ${highest_bid}")


while not bidding_finished:
    name = input("input yr name: ")
    bid_price = int(input("input your bid price here $: "))
    bids[name] = bid_price

    game_continue = input("is there any other bidder ? Type yes or no ").lower()

    if game_continue == "no":
        bidding_finished = True
        finding_highest_bidder(bids)

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bid_list = {}
new_bid_bool = True
while new_bid_bool:
    name = input("Bidder name:\t")
    bid = input("Bid price:\t$")
    bid_list[name] = float(bid)
    new_bid_bool = input("Are there more bidders? (True/False):\t")
    if new_bid_bool != "True":
        new_bid_bool = False
    else:
        new_bid_bool = True

    print("\n" * 10)

max_bid = 0

for name in bid_list:
    if bid_list[name] > max_bid:
        max_bidder = name

print(f"\n{max_bidder} is our winner!!")

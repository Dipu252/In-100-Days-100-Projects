import art

print(art.logo)

# TODO-1: Ask the user for input

bids = {}
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
continue_biding = True
while continue_biding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ")
    if should_continue == 'no':
        continue_biding = False
    else:
        print("\n" * 100)
# TODO-4: Compare bids in dictionary
# result = ("_",0)
# for key in bids:
#     if bids[key] > result[1]:
#         result = (key, bids[key])

name_winnwer = max(bids, key=bids.get)

print(f"The winmer is {name_winnwer} with a bid of ${bids[name_winnwer]}.")


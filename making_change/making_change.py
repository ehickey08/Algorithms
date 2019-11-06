#!/usr/bin/python

import sys

def making_change(amount, denominations):
    if amount <= 1:
        return 1
    count = 0
    for i, coin in enumerate(denominations):
        if amount - coin >= 0:
            count += making_change(amount - coin, denominations[:i+1])

    return count


print(making_change(22, [1,5,10,25,50]))
if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")

#!/usr/bin/python

import argparse


def find_max_profit(prices):
    current_min = prices[0]
    max_profit = float("-inf")

    for i in range(1, len(prices)):
        if (prices[i] - current_min) > max_profit:
            max_profit = prices[i] - current_min
        if prices[i] < current_min:
            current_min = prices[i]

    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer price')
    args = parser.parse_args()

    print(
        "A profit of ${profit} can be made from the stock prices {prices}.".format(
            profit=find_max_profit(args.integers), prices=args.integers))

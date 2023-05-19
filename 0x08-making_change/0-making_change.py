#!/usr/bin/python3

"""Making Change"""


def makeChange(coins, total):
    """determine the fewest number
    of coins needed to meet a given amount total."""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count_coin = 0
    for coin in coins:
        if coin <= total:
            count_coin += total // coin
            total = total % coin
        if total == 0:
            break
    if total != 0:
        return -1
    return count_coin

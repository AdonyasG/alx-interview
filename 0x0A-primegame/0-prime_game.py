#!/usr/bin/python3
"""
Prime Game
"""


def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    """
    if x == 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        prime_count = sum(is_prime(n) for n in range(1, num + 1))
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None

from numpy import random
from functools import lru_cache

coins = [50, 25, 10, 5, 2, 1]
change_cache = {}


def find_coins_greedy(change):
    change_coins = {}
    rest = change
    for coin in coins:
        coin_num = rest // coin
        if coin_num:
            change_coins[coin] = coin_num
            rest -= coin * coin_num
    return change_coins


def find_min_coins(change):
    global change_cache
    if change not in change_cache:
        change_cache[change] = find_coins_greedy(change)
    return change_cache[change]


@lru_cache
def find_min_coins_lru(change):
    return find_coins_greedy(change)

for _ in range(random.randint(64)):
    change = random.randint(200)
    print(change, find_coins_greedy(change))
    print(change, find_min_coins(change))
    print(change, find_min_coins_lru(change))

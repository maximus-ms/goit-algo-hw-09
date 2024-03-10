import timeit
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
            rest %= coin
        if rest == 0:
            break
    return change_coins


def find_min_coins(change):
    global change_cache
    if change not in change_cache:
        change_cache[change] = find_coins_greedy(change)
    return change_cache[change]


@lru_cache
def find_min_coins_lru(change):
    return find_coins_greedy(change)


def measure_exe_time(f_dict, iterations=100):
    exe_time = {f_n: 0 for f_n in f_dict.keys()}
    for _ in range(iterations):
        change = random.randint(200)
        for f_n, f in f_dict.items():
            exe_time[f_n] += timeit.timeit(lambda: f(change), number=1)
    return {f_n: t * 1000 for f_n, t in exe_time.items()}


if __name__ == "__main__":
    functions = {
        "greedy": find_coins_greedy,
        "min": find_min_coins,
        "min_lru": find_min_coins_lru,
    }
    exe_time = measure_exe_time(functions)

    print(f"Execution time before caching results:")
    for f_n, t in exe_time.items():
        print(f"\t{f_n:<7}: {t}")

    # "Train" and cache data
    exe_time = measure_exe_time(functions, iterations=50000)
    exe_time = measure_exe_time(functions)
    print(f"Execution time after caching results:")
    for f_n, t in exe_time.items():
        print(f"\t{f_n:<7}: {t}")

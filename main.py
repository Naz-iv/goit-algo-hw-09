import timeit
import matplotlib.pyplot as plt
from functools import partial
from collections import defaultdict, Counter

COINS = [1, 2, 5, 10, 25, 50]


def get_random_ints(length: int = 100) -> list[int]:
    return [i for i in range(11, length)]


def find_coins_greedy(change: int) -> dict:
    result = defaultdict(int)

    for coin in sorted(COINS, reverse=True):
        while change >= coin:
            result[coin] += 1
            change -= coin

    return result


def find_min_coins(change: int):
    dp = [float("inf")] * (change + 1)

    used_coins = [[] for _ in range(change + 1)]

    dp[0] = 0

    for coin in sorted(COINS, reverse=True):
        for i in range(coin, change + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used_coins[i] = used_coins[i - coin] + [coin]
    result = Counter(used_coins[change])

    return result

def visualize(tests: list, greedy: list, dynamic: list) -> None:
    plt.scatter(tests, greedy, color="blue", label="Greedy Times")
    plt.scatter(tests, dynamic, color="red", label="Dynamic Times")

    plt.title("Greedy vs Dynamic Execution Tme")
    plt.xlabel("Amounts")
    plt.ylabel("Time (s)")
    plt.grid(True)

    plt.show()


def main():
    execution_results = {
        "Greedy": [],
        "Dynamic": []
    }
    tests = get_random_ints(500)
    for change in tests:
        print(f"\nCoin = {change}\nExecution time:")

        greedy_time = timeit.timeit(partial(find_coins_greedy, change), number=100)
        dynamic_time = timeit.timeit(partial(find_min_coins, change), number=100)

        print(f"Greedy algorithm: {greedy_time}")
        print(f"Dynamic algorithm: {dynamic_time}")

        execution_results["Greedy"].append(greedy_time)
        execution_results["Dynamic"].append(dynamic_time)

    visualize(tests, execution_results["Greedy"], execution_results["Dynamic"])


if __name__ == "__main__":
    main()

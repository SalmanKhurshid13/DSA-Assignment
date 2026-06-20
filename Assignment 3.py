# Data Structures & Algorithms
# Assignment 3: Minimum Coins to Make All Values Obtainable

def minPatches(coins, target):
    coins.sort()

    patches = 0
    index = 0
    reachable = 0

    while reachable < target:

        if index < len(coins) and coins[index] <= reachable + 1:
            reachable += coins[index]
            index += 1

        else:
            # Add missing coin
            reachable += reachable + 1
            patches += 1

    return patches


# Taking input from user
coins = list(map(int, input("Enter coins separated by space: ").split()))
target = int(input("Enter target value: "))


result = minPatches(coins, target)

print("\nCoins:", coins)
print("Target:", target)
print("Minimum coins needed to add:", result)
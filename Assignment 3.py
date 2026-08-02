# --------------------------------------------
# Data Structures & Algorithms - Assignment 3
# Minimum Number of Coins to Add
# --------------------------------------------

def minimum_coins_to_add(coins, target):

    # Arrange the coins in ascending order
    coins.sort()

    added = 0          # Number of new coins added
    i = 0              # Current position in coin list
    covered = 0        # We can make every value from 1 to covered

    while covered < target:

        # Use the current coin if it extends the reachable range
        if i < len(coins) and coins[i] <= covered + 1:
            covered = covered + coins[i]
            i += 1

        else:
            # Add a new coin of value covered + 1
            new_coin = covered + 1
            added += 1
            covered = covered + new_coin

    return added


# ---------------------- Main Program ----------------------

print("Assignment 3 - Minimum Coins Problem")

try:

    n = int(input("Enter number of coins: "))

    if n < 0:
        print("Number of coins cannot be negative.")
        exit()

    coins = []

    if n > 0:
        print("Enter coin values:")
        for _ in range(n):
            value = int(input())

            if value <= 0:
                print("Coin values must be positive.")
                exit()

            coins.append(value)

    target = int(input("Enter target value: "))

    if target <= 0:
        print("Target must be greater than zero.")
        exit()

    answer = minimum_coins_to_add(coins, target)

    print("\nOriginal Coins :", coins)
    print("Target         :", target)
    print("Minimum Coins to Add :", answer)

except ValueError:
    print("Please enter valid integer values only.")
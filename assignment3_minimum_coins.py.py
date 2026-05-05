class Solution:
    def minimumAddedCoins(self, coins, target):
        coins.sort()
        
        miss = 1   # smallest value we cannot form
        i = 0
        count = 0
        
        while miss <= target:
            if i < len(coins) and coins[i] <= miss:
                miss += coins[i]
                i += 1
            else:
                # add a new coin = miss
                miss += miss
                count += 1
        
        return count


# Driver Code
coins = [1, 4, 10]
target = 19

sol = Solution()
print(sol.minimumAddedCoins(coins, target))  # Output: 2
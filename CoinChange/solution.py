class Solution(object):
    def coinChange(self, coins, amount):
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for cur_amount in range(1, amount+1):
            for cur_coin in coins:
                if cur_amount >= cur_coin:
                    dp[cur_amount] = min(dp[cur_amount], dp[cur_amount - cur_coin] + 1)
                    
        return dp[amount] if dp[amount] != amount + 1 else -1
    
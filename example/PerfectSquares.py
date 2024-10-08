# Дано целое число n, верните наименьшее количество чисел, являющихся совершенными квадратами, сумма которых равна n.

"""
Input: n = 13
Output: 2
"""

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        max_square_index = int(n**0.5) + 1
        square_nums = [i * i for i in range(max_square_index)]
        
        for i in range(1, n + 1):
            for s in range(1, max_square_index):
                if i < square_nums[s]:
                    break
                dp[i] = min(dp[i], dp[i - square_nums[s]] + 1)
        
        return dp[n]
    
if __name__ == "__main__":
    example = Solution()
    res = example.numSquares(n = 13)
    print(res)    
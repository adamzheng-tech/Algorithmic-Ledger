class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m): # Start strictly from index 1, because row 0 and column 0 are already solved.
            for j in range(1, n): 
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
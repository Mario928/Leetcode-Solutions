class Solution(object):
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n, dp = len(grid), len(grid[0]), [[0]*(len(grid[0]) + 1)] * 2
        dp[0][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i & 1][j] = dp[(i - 1) & 1][j] + dp[i & 1][j - 1] if not grid[i - 1][j - 1] else 0
        return dp[m & 1][-1]
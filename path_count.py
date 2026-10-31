class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[c+1] represents [ways arriving moving right, ways arriving moving down] at column c
        dp = [[0, 0] for _ in range(n + 1)]
        dp[1] = [1, 1]  # Base case setup for the starting point
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    # Mirror cell reflection: 
                    # Right incoming turns Down, Down incoming turns Right
                    dp[c+1] = [dp[c+1][1], dp[c][0]]
                else:
                    # Empty cell: paths combine from both directions
                    val = (dp[c+1][1] + dp[c][0]) % MOD
                    dp[c+1] = [val, val]
                    
        return dp[-1][0]

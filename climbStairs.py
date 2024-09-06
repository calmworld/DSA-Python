"""
Approach 1: Recursion
Explanation: The recursive solution uses the concept of Fibonacci numbers to solve the problem.
It calculates the number of ways to climb the stairs by recursively calling the climbStairs function for (n-1) and (n-2) steps.
However, this solution has exponential time complexity (O(2^n)) due to redundant calculations.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)



# Create an instance of the Solution class
solution = Solution()

# Call the climbStairs method on the instance
print(solution.climbStairs(4)) # 5

"""
Approach 2: Memoization
Explanation: The memoization solution improves the recursive solution by introducing memoization, which avoids redundant calculations.
We use an unordered map (memo) to store the already computed results for each step n. Before making a recursive call, we check if the result for the given n exists in the memo.
If it does, we return the stored value; otherwise, we compute the result recursively and store it in the memo for future reference.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)

    def helper(self, n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]

# Create an instance of the Solution class
solution = Solution()

# Call the climbStairs method on the instance
print(solution.climbStairs(4)) # 5


"""
Approach 3: Tabulation
Explanation: The tabulation solution eliminates recursion and uses a bottom-up approach to solve the problem iteratively.
It creates a DP table (dp) of size n+1 to store the number of ways to reach each step. The base cases (0 and 1 steps) are initialized to 1 since there is only one way to reach them. Then, it iterates from 2 to n, filling in the DP table by summing up the values for the previous two steps.
Finally, it returns the value in the last cell of the DP table, which represents the total number of ways to reach the top.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


# Create an instance of the Solution class
solution = Solution()

# Call the climbStairs method on the instance
print(solution.climbStairs(4)) # 5


"""
Approach 4: Space Optimization
Explanation: The space-optimized solution further reduces the space complexity by using only two variables (prev and curr) instead of an entire DP table.
It initializes prev and curr to 1 since there is only one way to reach the base cases (0 and 1 steps).
Then, in each iteration, it updates prev and curr by shifting their values. curr becomes the sum of the previous two values, and prev stores the previous value of curr.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n+1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr



# Create an instance of the Solution class
solution = Solution()

# Call the climbStairs method on the instance
print(solution.climbStairs(4)) # 5



class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Time Complexity = O(N)
        Space Complexity = O(1)
        '''
        not_taken = 0 
        taken = nums[0]
        for row in range(1, len(nums)):
            prev_not_taken = not_taken
            not_taken = max( prev_not_taken , taken  )
            taken = prev_not_taken + nums[row]
        return max( not_taken, taken )
        
    def subOptimalrob(self, nums: List[int]) -> int:
        '''
        Algorithm:
        We make a dp array for not taken case and taken case for each value. 
        for a particular house, if we do not take it, then we take the max from the prev case 
        for a particular house, if we take it, we add the prev value's no taken with the present value
        
        Finally we return the maximum of taken and not taken for the last cell's value as that will be the cummilative of all different cases. 
        
        Time Complexity = O(N)
        Space Complexity = O(N*2)
        '''
        dp = [ [ 0 ,0 ] for x in range(len(nums)) ]
        # print(dp)
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for row in range(1, len(nums)):
            dp[row][0] = max(dp[row-1][0], dp[row-1][1])
            dp[row][1] = dp[row-1][0] +  nums[row]
        return max( dp[-1][0] , dp[-1][1] )

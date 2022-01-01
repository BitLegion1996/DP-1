class BruteForceSolution:
    '''
    Time Limit Exceeded 
    Algorithm :
    We can either choose a coin and reduce the amount or 
    not choose a coin and increment the index by 1 
    but for each iterative call we pass the number of coins used with the 
    function call 
    
    '''
    def helper(self, coins, amount, index, coins_used):
        if amount == 0 :
            return coins_used
        if amount < 0:
            return -1 
        if index >= len(coins):
            return -1
        choose_a_coin_case = self.helper(coins, amount - coins[index], index, coins_used+1 )
        not_choose_a_coin_case = self.helper(coins, amount, index+1, coins_used )
        if choose_a_coin_case  == -1 :
            return not_choose_a_coin_case 
        if not_choose_a_coin_case == -1 :
            return choose_a_coin_case 
        return min(choose_a_coin_case  , not_choose_a_coin_case )
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.helper(coins, amount, 0, 0)

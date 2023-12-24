class solution:
    def coinChange(self, coins, amount):
            # Sort the coins in descending order
        coins.sort(reverse = True)
        length = len(coins)
        i = 0
        while(amount>0):
            if(coins[i]<=amount):
                print ("Use coin of denomination: ", coins[i])
                amount = amount - coins[i]
            else:
                i += 1

obj = solution()
obj.coinChange([1, 2, 5, 10, 20, 50, 100, 500, 1000], 93)
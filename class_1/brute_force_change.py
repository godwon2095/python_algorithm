# -*- coding: utf-8 -*-
def brute_force_change_helper(coinList, value):
    
    def brute_force_change(coins, change):
        minCoins = [0 for c in coins]
        minCoins[0] = change

        for coin in [c for c in coins if c <= change]:
            temp = (brute_force_change(coins, change - coin))
            temp[coins.index(coin)] += 1
            if sum(minCoins) > sum(temp):
                minCoins = temp
                bestSum = temp
        return (minCoins)
        
    finalCoins = brute_force_change(coinList, value)  
    coinSum = sum(finalCoins)
           
    return (finalCoins, coinSum)


coins = [25, 20, 10, 5, 1]
result = brute_force_change_helper(coins, 40)

print ("가장 좋은 코인 조합: {}, 필요한 동전의 수: {}".format(result[0], result[1]))
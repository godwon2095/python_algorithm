# 수학과 2015110417 장성원
# -*- coding: utf-8 -*-
def brute_force_change_helper(coin_list, value):
    
    def brute_force_change(coins, change):
        min_coins = [0 for c in coins]
        min_coins[0] = change

        for coin in [c for c in coins if c <= change]:
            temp = (brute_force_change(coins, change - coin))
            temp[coins.index(coin)] += 1
            if sum(min_coins) > sum(temp):
                min_coins = temp
                best_sum = temp
        return (min_coins)
        
    final_coins = brute_force_change(coin_list, value)  
    coin_sum = sum(final_coins)
           
    return (final_coins, coin_sum)


coins = [25, 20, 10, 5, 1]
result = brute_force_change_helper(coins, 40)

print ("가장 좋은 코인 조합: {}, 필요한 동전의 수: {}".format(result[0], result[1]))
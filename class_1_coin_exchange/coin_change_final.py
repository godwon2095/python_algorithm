# -*- coding: utf-8 -*-
def better_greedy_change(M, coins):
    results = []
    count = 0
    for coin in coins:
        k = M // coin
        results.append(k)
        M = M - coin * k
        count += k
    return (results, count)


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

coins = [25, 20, 15, 10, 5, 1]

for count in range(1, 100):
    b_g_result = better_greedy_change(count, coins)
    b_f_result = brute_force_change_helper(coins, count)
    if b_g_result[0] != b_f_result[0]:
        print('better greedy 코인조합: {}, 동전의 수: {}'.format(b_g_result[0], b_g_result[1]))
        print('brute force 코인조합: {}, 동전의 수: {}\n'.format(b_f_result[0], b_f_result[1]))
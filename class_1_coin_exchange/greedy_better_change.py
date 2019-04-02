# 수학과 2015110417 장성원
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

coins = [25, 20, 10, 5, 1]
print("코인의 조합: {}, 코인의 수: {}".format(better_greedy_change(40, coins)[0], better_greedy_change(40, coins)[1]))
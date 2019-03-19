# 2015110417 수학과 장성원
# -*- coding: utf-8 -*-
import pdb;

def GreedyRecursive(coins, count, M, result):
    if M >= coins[count]:
        k = M // coins[count]
        M = M - coins[count] * k
        result += k
    count += 1
    if M == 0:
        return result
    else:
        return GreedyRecursive(coins, count, M, result)

coins = [35, 30, 20, 15, 5]
result = 0
M = 60
count = 0
print(GreedyRecursive(coins, count, M, result))

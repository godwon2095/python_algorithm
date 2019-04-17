# 수학과 2015110417 장성원
# -*- coding: utf-8 -*-
# 감점 당함 ㅠㅠ
import pdb

def greedyDP(coin_list, M, known_results):
   min_coins = M
   used_coins = []

   if M in coin_list:
      known_results[M] = 1
      return 1
   elif known_results[M] > 0:
      return known_results[M]
   else:
       for i in [c for c in coin_list if c <= M]:
         num_coins = 1 + greedyDP(coin_list, M - i, known_results)

         if num_coins < min_coins:
            min_coins = num_coins
            known_results[M] = min_coins
   print(used_coins)
   return min_coins


print(greedyDP([1, 3, 5], 11, [0]*12))

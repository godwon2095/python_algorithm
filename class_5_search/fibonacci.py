#2015110417 수학과 장성원
# -*- coding: utf-8 -*-
import pdb

storage = [0 for i in range(100)]

def Fibonacci(num):
    if num == 1 or num == 2: 
        return 1
    if storage[num] != 0:
        return storage[num]
    storage[num] = Fibonacci(num - 1) + Fibonacci(num - 2)
    return storage[num]


for i in range(1, 21):
    print(Fibonacci(i))
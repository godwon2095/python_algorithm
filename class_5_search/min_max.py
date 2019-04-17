#2015110417 수학과 장성원
# -*- coding: utf-8 -*-
import pdb
from random import *

def Minimun(num_list):
    temp = num_list[0]
    for num in num_list[1:]:
        if num < temp:
            temp = num
    return temp


def Maximun(num_list):
    temp = num_list[0]
    for num in num_list[1:]:
        if num > temp:
            temp = num
    return temp


def FindMinMax(num_list):
    temp1, temp2 = num_list[0], num_list[0]
    for num in num_list[1:]:
        if num > temp1:
            temp1 = num
        if num < temp2:
            temp2 = num
    return print("Min: {}, Max: {}".format(temp2, temp1))


ran_num_list = sample([i for i in range(1, 100001)], 1000)
print(Minimun(ran_num_list))
print(Maximun(ran_num_list))
FindMinMax(ran_num_list)
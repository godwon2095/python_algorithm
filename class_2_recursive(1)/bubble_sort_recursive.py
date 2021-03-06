#2015110417 수학과 장성원
# -*- coding: utf-8 -*-
import pdb;

def Swap(num_list, index):
    num_list[index], num_list[index - 1] = num_list[index - 1], num_list[index]


def BubbleSortRecursive(num_list):
    count = 0
    for index, num in enumerate(num_list):
        if index - 1 >= 0 and num_list[index - 1] > num:
            Swap(num_list, index)
            print(num_list)
            count += 1
    if count == 0:
        return print("정렬 결과 : {}".format(num_list))
    else:
        return BubbleSortRecursive(num_list)


num_list = [30, 20, 40, 10, 5, 10, 30, 15]
BubbleSortRecursive(num_list)
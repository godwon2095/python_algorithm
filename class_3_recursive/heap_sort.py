#2015110417 수학과 장성원
# -*- coding: utf-8 -*-
import pdb


def heapify(num_list, index, size):
    __max__ = index
    left= index * 2 + 1
    right = index * 2 + 2

    if left < size and num_list[left] > num_list[__max__]:
        __max__ = left

    if right < size and num_list[right] > num_list[__max__]:
        __max__ = right

    if __max__ != index:
        num_list[index], num_list[__max__] = num_list[__max__], num_list[index]
        heapify(num_list, __max__, size)
        
    print(num_list)


def HeapSort(num_list):
    length = len(num_list)

    for i in range(length // 2 - 1, -1, -1):
        heapify(num_list, i, length)

    for i in range(length - 1, 0, -1):
        num_list[0], num_list[i] = num_list[i], num_list[0]
        heapify(num_list, 0, i)
        
    print("result : {}".format(num_list))



num_list =  [4, 4, 3, 2, 16, 9, 10, 14, 9, 10, 7]
HeapSort(num_list)
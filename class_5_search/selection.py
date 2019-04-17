#2015110417 수학과 장성원
# -*- coding: utf-8 -*-
import pdb

def Selection(num_list, order):

    def select(list, left, right, index):
        if right == left:
            return list[left]

        pivot_index = 5
        list[left], list[pivot_index] = list[pivot_index], list[left]

        i = left
        for j in range(left + 1, right + 1):
            if list[j] < list[left]:
                i += 1
                list[i], list[j] = list[j], list[i]

        list[i], list[left] = list[left], list[i]

        if index == i:
            return list[i]
        elif index < i:
            return select(list, left, i - 1, index)
        else:
            return select(list, i + 1, right, index)

    if num_list is None or len(num_list) < 1:
        return None

    if order < 0 or order > len(num_list) - 1:
        raise IndexError()

    return select(num_list, 0, len(num_list) - 1, order)


num_list = [10, 58, 18, 3, 29, 2, 90, 26, 34, 53,
            11, 23, 21, 4, 52, 1, 36, 27, 33, 57,
            15, 55, 22, 5, 80, 14, 45, 30, 88,
            17, 50, 25, 6, 81, 8, 40, 35, 70,
            20, 12, 28, 9, 89, 7, 24, 60, 71]

order = 17
print('{}번째로 작은 원소는 {}입니다.'.format(order, Selection(num_list, order)))

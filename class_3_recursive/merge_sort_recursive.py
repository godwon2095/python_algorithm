#2015110417 수학과 장성원
# -*- coding: utf-8 -*-
import pdb

def MergePartial(left_list, right_list):
    sorted_list = []
    while len(left_list) > 0 or len(right_list) > 0:
        if len(left_list) > 0 and len(right_list) > 0:
            if left_list[0] <= right_list[0]:
                sorted_list.append(left_list[0])
                left_list = left_list[1:]
            else:
                sorted_list.append(right_list[0])
                right_list = right_list[1:]
        elif len(left_list) > 0:
            sorted_list.append(left_list[0])
            left_list = left_list[1:]
        elif len(right_list) > 0:
            sorted_list.append(right_list[0])
            right_list = right_list[1:]
    return sorted_list


def MergeSort(num_list):
    if len(num_list) <= 1:
        return num_list

    mid = len(num_list) // 2
    left_list = num_list[:mid]
    right_list = num_list[mid:]

    left_list = MergeSort(left_list)
    right_list = MergeSort(right_list)
    print(num_list)
    return MergePartial(left_list, right_list)


num_list = [1.5, 1, 2, 5, 2.5, 2.25, 0.5, 12.5, 7.5]
print(MergeSort(num_list))
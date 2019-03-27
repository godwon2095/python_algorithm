#2015110417 수학과 장성원
# -*- coding: utf-8 -*-
import pdb


def BucketSort(num_list):
    __max__ = max(num_list)
    length = len(num_list)
    size = __max__ / length
 
    buckets = [[] for _ in range(length)]
    ## 2차원 list로 입력된 숫자 리스트의 길이만큼 배열을 생성해준다

    for i in range(length):
        j = int(num_list[i] / size)
        if j == length:
            buckets[length - 1].append(num_list[i])
        else:
            buckets[j].append(num_list[i])
 
    for i in range(length):
        quick_sort(buckets[i])
        ## or
        # insertion_sort(buckets[i]) 
 
    result = []
    for i in range(length):
        result = result + buckets[i]
 
    return result
 
def insertion_sort(num_list):
    for i in range(1, len(num_list)):
        temp = num_list[i]
        j = i - 1
        while (j >= 0 and temp < num_list[j]):
            num_list[j + 1] = num_list[j]
            j = j - 1
        num_list[j + 1] = temp


def quick_sort(num_list):
    length = len(num_list)
    if length <= 1:
        return num_list
    else:
        pivot = num_list[0]
        grator = [ element for element in num_list[1:] if element > pivot ]
        lessor = [ element for element in num_list[1:] if element <= pivot ]
        return quick_sort(lessor) + [pivot] + quick_sort(grator)
 

num_list =  [9.9, 1.0, 5.5, 5.7, 3.4, 1.2, 8.3, 1.0, 0.0]
list_b = [3.8, 7.2, 16.2, 0.8, 9.8, 10.9, 30.0, 20.7, 5.2, 19.3, 4.9, 21.3] 
print(BucketSort(list_b))
#2015110417 수학과 장성원
# -*- coding: utf-8 -*-
import pdb

def MergePartial(a, b):
    sorted_list = []
    c1, c2 = 0, 0
                                                      
    while((c1 < len(a)) and (c2 < len(b))):

        if(a[c1] > b[c2]):
            sorted_list.append(b[c2])
            c2 += 1
        elif(a[c1] < b[c2]): 
            sorted_list.append(a[c1])
            c1 += 1
        elif(a[c1] == b[c2]):
            sorted_list.append(a[c1])
            sorted_list.append(b[c1])
            c1, c2 = c1 + 1, c2 + 1

    if(c1 < len(a)):
        for k in range(c1, len(a)):
            sorted_list.append(a[k])
    elif(c2 < len(b)):
        for h in range(c2, len(b)):
            sorted_list.append(b[h])

    return sorted_list
    

def MergeSort(num_list):
    result_list = []

    for i in range(len(num_list)):
        temp = [num_list[i]]
        result_list.append(temp)

    while(len(result_list) != 1):  
        j = 0
                                                
        while(j < len(result_list)-1): 
            temp_list = MergePartial(result_list[j], result_list[j+1])
            result_list[j] = temp_list
            del result_list[j+1]
            j = j+1
        print(result_list)
    print(result_list[0])


num_list = [1.5, 1, 2, 5, 2.5, 2.25, 0.5, 12.5, 7.5]
MergeSort(num_list)
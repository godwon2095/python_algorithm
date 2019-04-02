# 수학과 2015110417 장성원
# -*- coding: utf-8 -*-
import pdb

def bacteria_vs_virus(defaul_bacteria_count):
    bacteria_count = defaul_bacteria_count
    virus_count = 1

    if defaul_bacteria_count < 1:
        return
    else:
        for i in range(1, defaul_bacteria_count + 1):
            bacteria_count = 2 * (bacteria_count - virus_count)
            virus_count *= 2
            print("time: {}min, virus: {},  bacteria: {}".format(i, virus_count, bacteria_count))


bacteria_vs_virus(30)
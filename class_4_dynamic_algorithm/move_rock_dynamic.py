# 수학과 2015110417 장성원
# -*- coding: utf-8 -*-
# 감점당함 ㅜ.ㅠ
import pdb


def moveRocksDP(m, n):
    known_results = [[0]*n for i in range(m)] # m 행 n 열의 2차원 리스트(배열) 생성
    known_results[0][0] = 'O'
    known_results[0][1] = 'W'
    known_results[1][0] = 'W'
    known_results[1][1] = 'W'

    for i, row in enumerate(known_results):
        for j, item in enumerate(row):
            if known_results[i][j] != 0:
                continue
            elif i == 0:
                if known_results[i][j-1] == 'W':
                    known_results[i][j] = 'L'
                else:
                    known_results[i][j] = 'W'
            elif j == 0:
                if known_results[i-1][j] == 'W':
                    known_results[i][j] = 'L'
                else:
                    known_results[i][j] = 'W'
            else:
                if known_results[i-1][j] == 'W' and known_results[i][j-1] == 'W' and known_results[i-1][j-1] == 'W':
                    known_results[i][j] = 'L'
                else:
                    known_results[i][j] = 'W'

    return known_results


m, n = 10, 7

for i in moveRocksDP(m + 1, n + 1):
    print(i)

# -*- coding: utf-8 -*-
num_list_str = input('정수 리스트를 입력해주세요:').split(',')
max_N = 20

default_sum = sum(x for x in range(1, max_N + 1) if x % 2 == 0)

input_sum = 0
for num in num_list_str:
    input_sum += int(num)

excluded_num = default_sum - input_sum
print('제외 된 짝수는 {} 입니다.'.format(excluded_num))

#2015110417 수학과 장성원
# -*- coding: utf-8 -*-
import pdb, random

# myGenomeSeq 을 만들기 위한 메소드
def generateSequences(N):
    bases = ('A', 'C', 'G', 'T')
    seq = ''.join([random.choice(bases) for _ in range(N)])
    return seq


# 정렬을 위한 quick sort 메소드
def quickSort(num_list):
    length = len(num_list)
    if length <= 1:
        return num_list
    else:
        pivot = num_list[0]
        grator = [ element for element in num_list[1:] if element > pivot ]
        lessor = [ element for element in num_list[1:] if element <= pivot ]
        return quickSort(lessor) + [pivot] + quickSort(grator)


N = 1000000
L = 50
M = 20000
myGenomeSeq = generateSequences(N)
rand_indexes = quickSort(random.sample(range(N - L), M))

# coverage 의 총합
sum_of_coverage = 0

# myGenomeSeq 을 하나씩 돌면서
for i in range(1, N + 1):
    coverage = 0
    # 50보다 작은 경우는 1~i 까지 위에서 뽑은 rand_index 가 해당 범위에 포함될 경우 coverage 값을 더해준다
    if i < 50:
        for rand_index in rand_indexes:
            if rand_index in range(1, i):
                coverage += 1
        print("site {}의 coverage: {}".format(i, coverage))
        sum_of_coverage += coverage
    # 50보다 크거나 같은 경우는 i-49~i 까지 위에서 뽑은 rand_index 가 해당 범위에 포함될 경우 coverage 값을 더해준다
    else:
        for rand_index in rand_indexes:
            if rand_index in range(i - 49, i):
                coverage += 1
        print("site {}의 coverage: {}".format(i, coverage))
        sum_of_coverage += coverage

print("MyGenomeSeq 의 평균 coverage: {}".format(sum_of_coverage / M))

#2015110417 수학과 장성원
# -*- coding: utf-8 -*-
import pdb, random, string

def generateSequences(N):
    bases = ('A', 'C', 'G', 'T')
    seq = ''.join([random.choice(bases) for _ in range(N)])
    return seq

N = 1000000
L = 50
M = 20000
myGenomeSeq = generateSequences(N)
rand_indexes = random.sample(range(N - L), M)
text_file = open("reads.txt", "w")

# 파일에 short read 를 적는 부분
for index in rand_indexes:
    short_read = myGenomeSeq[index:index+L]
    text_file.write(short_read)
text_file.close()


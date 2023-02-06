# 삼총사
# 풀이 시간 : 30분

from itertools import combinations


def solution(number):
    nCr = combinations(number, 3)
    return [sum(c) for c in nCr].count(0)

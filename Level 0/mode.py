# 최빈값 구하기
from collections import Counter


def solution(array):
    counter = Counter(array)
    sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    if len(sorted_counter) == 1:
        return sorted_counter[0][0]
    else:
        if sorted_counter[0][1] == sorted_counter[1][1]:
            return -1
        else:
            return sorted_counter[0][0]


solution([1, 1, 1, 2, 3, 3, 3, 4])

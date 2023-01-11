# 문자열 내 p와 y의 개수


def solution(s):
    low = s.lower()
    return low.count("p") == low.count("y")


# 해시를 이용하여 시간복잡도 줄이기

from collections import Counter


def solution(s):
    count = Counter(s.lower())
    return count["p"] == count["y"]

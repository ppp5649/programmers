# 모의고사
# 풀이 시간 : 40분 + 30분 총 1시간 10분

import math


def solution(answers):
    test1 = [1, 2, 3, 4, 5] * math.ceil(len(answers) / 5)
    test2 = [2, 1, 2, 3, 2, 4, 2, 5] * math.ceil(len(answers) / 8)
    test3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * math.ceil(len(answers) / 10)

    cnt = [0, 0, 0]

    for t1, answer in zip(test1[: len(answers)], answers):
        if t1 == answer:
            cnt[0] += 1

    for t2, answer in zip(test2[: len(answers)], answers):
        if t2 == answer:
            cnt[1] += 1

    for t3, answer in zip(test3[: len(answers)], answers):
        if t3 == answer:
            cnt[2] += 1

    # # max값 index 여러개(filter 사용)
    # rank = list(filter(lambda x: cnt[x] == max(cnt), range(len(cnt))))

    # max값 index 여러개(enumerate 사용)
    rank = [i + 1 for i, c in enumerate(cnt) if c == max(cnt)]

    return rank

# 2019 카카오 > 실패율
# 풀이 시간 : 1시간 (실패)

from collections import Counter


def solution(n, stages):
    stages.sort()
    # print(stages)
    fail = Counter(stages)
    trial = {i: 0 for i in range(1, n + 2)}
    trial[1] = len(stages)

    for i in range(len(stages) - 1):
        if stages[i] != stages[i + 1]:
            trial[stages[i] + 1] += len(stages) - i - 1

    for i in range(1, n + 1):
        if fail[i] == 0:
            trial[i + 1] = 1000000
    print(fail)
    print(trial)
    rate = {i: (fail[i] / trial[i]) for i in range(1, n + 1)}
    rank = sorted(rate.items(), key=lambda x: x[1], reverse=True)

    return [r[0] for r in rank]


# 1시간 풀이 후 실패 -> 30분 추가 풀이 총 1시간 30분
from collections import Counter


def solution(N, stages):
    stages.sort()

    rate = Counter(stages)
    rate[stages[0]] = stages.count(stages[0]) / len(stages)

    for i in range(len(stages) - 1):
        if stages[i] != stages[i + 1]:
            rate[stages[i + 1]] = stages.count(stages[i + 1]) / len(stages[i + 1 :])

    del rate[N + 1]
    st_rate = sorted(rate.items(), key=lambda x: x[1], reverse=True)
    answer = [r[0] for r in st_rate]

    num = 1
    while N != len(answer):
        if num not in answer:
            answer.append(num)
        num += 1

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

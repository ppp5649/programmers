# 탐욕법(Greedy) > 체육복
# 풀이 시간 : 20분


def solution(n, lost, reserve):
    suit = {i: 1 for i in range(1, n + 1)}
    answer = 0

    for l in lost:
        suit[l] -= 1

    for r in reserve:
        suit[r] += 1

    if suit[1] == 0 and suit[2] == 2:
        suit[1] += 1
        suit[2] -= 1

    for i in range(2, n):
        if suit[i] == 0 and suit[i - 1] == 2:
            suit[i] += 1
            suit[i - 1] -= 1

        elif suit[i] == 0 and suit[i + 1] == 2:
            suit[i] += 1
            suit[i + 1] -= 1

    if suit[n] == 0 and suit[n - 1] == 2:
        suit[n] += 1
        suit[n - 1] -= 1

    for k in suit:
        if suit[k] > 0:
            answer += 1

    return answer

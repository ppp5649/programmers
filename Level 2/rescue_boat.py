# 탐욕법(Greedy) > 구명보트
# 풀이 시간 : 25분 (combinations 부터 바로 시간초과 - O(N^2)이라 그런듯)

from itertools import combinations


def solution(people, limit):
    answer = 0
    c = list(combinations(people, 2))
    idx_c = list(combinations(range(len(people)), 2))
    couple = []
    idx_arr = [i for i in range(len(people))]

    for i in range(len(c)):
        if sum(c[i]) <= limit:
            couple.append((sum(c[i]), idx_c[i]))

    couple.sort(reverse=True)
    for c in couple:
        if c[1][0] in idx_arr and c[1][1] in idx_arr:
            idx_arr.remove(c[1][0])
            idx_arr.remove(c[1][1])
            answer += 1

    answer = answer + len(idx_arr)

    return answer


# %%

# deque를 이용한 풀이
# 핵심 아이디어는 정렬 후 최솟값과 최댓값의 합을 limit과 비교
from collections import deque


def solution(people, limit):
    answer = 0
    people.sort()
    deq = deque(people)

    while len(deq) > 0:
        if deq[0] + deq[-1] <= limit:
            if len(deq) > 1:
                deq.popleft()
                deq.pop()
            else:
                deq.pop()

        else:
            deq.pop()

        answer += 1

    return answer


print(solution([70, 80, 50], 100))

# %%

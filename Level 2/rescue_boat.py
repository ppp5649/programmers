# 탐욕법(Greedy) > 구명보트
# 풀이 시간 : 50분 (풀지 못함)

from itertools import combinations
from collections import Counter


def solution(people, limit):
    answer = 0
    p_dic = Counter(people)
    nC2 = combinations(people, 2)

    for c in nC2:
        if sum(c) <= limit:
            if p_dic[c[0]] > 0 and p_dic[c[1]] > 0:
                p_dic[c[0]] -= 1
                p_dic[c[1]] -= 1
                answer += 1

    for k, v in p_dic.items():
        answer += v

    return answer


solution([80, 50, 40, 40, 50, 70], 120)

from collections import deque


def solution(people, limit):
    answer = 0
    people = deque(sorted(people))

    for _ in range(len(people)):
        if people:
            people.pop()
            people.popleft()
            answer += 1

    return answer


print(solution([80, 50, 40, 40, 50, 70], 120))

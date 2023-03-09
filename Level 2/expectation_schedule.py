# 예상 대진표
# 풀이 시간 : 10분

# 1 2 -> 1 3 4 -> 2
from math import ceil


def solution(n, a, b):
    answer = 0

    while a != b:
        a = ceil(a / 2)
        b = ceil(b / 2)
        answer += 1

    return answer


# math 안쓰고 몫을 이용한 풀이 - 1 더한 몫과 나머지까지 확인하는 습관


def solution(n, a, b):
    answer = 0

    while a != b:
        a, b = (a + 1) // 2, (b + 1) // 2
        answer += 1

    return answer

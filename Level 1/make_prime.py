# 소수 만들기
# 풀이 시간 : 7분

from itertools import combinations


def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def solution(nums):
    return sum([is_prime(sum(c)) for c in combinations(nums, 3)])

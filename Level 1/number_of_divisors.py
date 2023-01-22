# 약수의 개수와 덧셈
# 풀이 시간 : 20분


def cnt_divisors(n):
    count = 1

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            count += 1

    return count


def solution(a, b):

    return sum([n if cnt_divisors(n) % 2 == 0 else -n for n in range(a, b + 1)])


# 제곱수의 성질을 이용한 풀이
# 제곱수의 약수의 개수는 홀수 제곱수가 아닌 수의 약수의 개수는 짝수
def solution(a, b):
    return sum([-n if n**0.5 == int(n**0.5) else n for n in range(a, b + 1)])


# 리스트 만들어서 sum 하는 것 보다 for문 돌면서 더하는 게 속도는 빠름
from math import sqrt


def solution(left, right):
    answer = 0

    for n in range(left, right + 1):
        answer += -n if sqrt(n) == int(sqrt(n)) else n

    return answer

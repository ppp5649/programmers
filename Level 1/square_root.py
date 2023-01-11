# 정수 제곱근 판별
# math.floor()과 math.ceil()의 값이 같을 때 정수라고 판별함

from math import floor, ceil


def square_root(n):
    if floor(n**0.5) == ceil(n**0.5):
        return (n**0.5 + 1) ** 2
    else:
        return -1


# 정수 판별법(1) - 1로 나눈 나머지를 이용한 방법


def square_root(n):
    sqrt = n**0.5
    return (sqrt + 1) ** 2 if sqrt % 1 == 0 else -1


# 정수 판별법(2) - n 자체와 int(n)이 같은지 비교하는 방법


def square_root(n):
    sqrt = n**0.5
    return (sqrt + 1) ** 2 if sqrt == int(sqrt) else -1

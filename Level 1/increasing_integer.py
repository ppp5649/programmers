# x만큼 간격이 있는 n개의 숫자
# range 함수의 3번째 parameter에는 0이 들어갈 수 없음


def increasing_integer(x, n):
    if x == 0:
        return [0] * n
    else:
        return [i for i in range(x, (n + 1) * x, x)]


# 다른 풀이


def increasing_integer(x, n):
    return [x + i * x for i in range(n)]

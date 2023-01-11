# 약수의 합


def add_divisor(n):
    return sum([i for i in range(1, n + 1) if n % i == 0])


# 사실상 n은 n의 약수에 포함되니까 n//2 까지만 검사하고 n만 더해주면 됨
# 탐색 갯수가 n/2개나 줄어듬


def add_divisor(n):
    return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])

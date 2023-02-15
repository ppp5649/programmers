# 피보나치 수
# 풀이 시간 : 6분


def solution(n):
    f = [0, 1]
    while len(f) < n + 1:
        f.append(f[-1] + f[-2])

    return f[-1] % 1234567

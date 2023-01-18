# 나머지가 1이 되는 수 찾기
# 풀이 시간 : 2분


def find_remainder(n):
    for i in range(1, n + 1):
        if n % i == 1:
            return i

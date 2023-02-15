# 다음 큰 숫자
# 풀이 시간 : 7분


def solution(n):
    cnt = 0
    num = n

    while cnt != bin(n)[2:].count("1"):
        num += 1
        cnt = bin(num)[2:].count("1")

    return num

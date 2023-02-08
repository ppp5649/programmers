# 소수 찾기
# 풀이 시간 : 50분 +


def cnt_divisor(k):
    divisor = [i for i in range(2, k // 2 + 1) if k % i == 0]

    return len(divisor)


def solution(n):
    answer = 0
    for i in range(2, n + 1):
        if cnt_divisor(i) == 0:
            answer += 1

    return answer

# 없는 숫자 더하기
# 풀이 시간 : 5분


def solution(numbers):
    return sum(set(range(10)) - set(numbers))

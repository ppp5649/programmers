# 정수 내림차순으로 배치하기
# 풀이 시간 : 6분


def solution(n):
    return int("".join(sorted(str(n), reverse=True)))

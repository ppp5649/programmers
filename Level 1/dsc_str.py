# 문자열 내림차순으로 배치하기
# 풀이 시간 : 4분


def solution(s):
    return "".join(sorted(s, reverse=True))

# 가운데 글자 가져오기
# 풀이 시간 : 10분
# 홀수와 짝수의 성질을 잘 생각하면 더 쉽게 풀 수 있음


def solution(s):
    l = len(s) // 2
    return s[l - 1 : l + 1] if len(s) % 2 == 0 else s[l]


def solution(s):
    return s[(len(s) - 1) // 2 : len(s) // 2 + 1]

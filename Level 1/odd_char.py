# 이상한 문자 만들기
# 풀이 시간 : 40분
# 공백이 2개이상 일때가 관건


def solution(s):
    answer = ""
    idx = 0

    for c in s:
        if c == " ":
            idx = 1
            answer += " "

        else:
            answer += c.upper() if idx % 2 == 0 else c.lower()

        idx += 1

    return answer

# 시저 암호
# 풀이 시간 : 20분


def solution(s, n):
    answer = ""

    small = [chr(i) for i in range(97, 123)]
    small += small
    big = [chr(i) for i in range(65, 91)]
    big += big

    for c in s:
        if c == " ":
            answer += " "
        elif c in small:
            answer += small[small.index(c) + n]
        else:
            answer += big[big.index(c) + n]

    return answer

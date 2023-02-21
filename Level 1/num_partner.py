# 숫자 짝꿍
# 풀이 시간 : 30분

from collections import Counter


def solution(X, Y):
    answer = ""
    X = Counter(X)
    Y = Counter(Y)

    for i in range(9, -1, -1):
        mn = min(X[str(i)], Y[str(i)])
        answer += str(i) * mn

    # 겹치는게 없는 경우
    if answer == "":
        return "-1"

    # 0으로만 이루어진 경우
    # int(answer) == 0 인 경우로 조건을 걸었더니 answer의 길이가 긴 경우 시간초과
    # 숫자는 0으로 시작할 수 없으므로 answer[0]만 "0"인지 확인하면 됨
    if answer[0] == "0":
        return "0"

    return answer

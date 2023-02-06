# K번째수
# 풀이 시간 : 7분


def solution(array, commands):
    answer = []
    for c in commands:
        answer.append(sorted(array[c[0] - 1 : c[1]])[c[2] - 1])

    return answer

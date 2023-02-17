# 과일 장수
# 풀이 시간 : 8분


def solution(k, m, score):
    answer = 0
    score.sort()
    box = []

    while len(score) >= m:
        for _ in range(m):
            box.append(score.pop())
        answer += min(box) * m
        box.clear()

    return answer


def solution(k, m, score):
    answer = 0
    score.sort()

    while len(score) >= m:
        box = score[-m:]
        answer += min(box) * m
        del score[-m:]

    return answer


print(solution(3, 4, [1, 1, 2, 3, 1, 2, 3, 1]))

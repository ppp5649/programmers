# 명예의 전당
# 풀이 시간 : 20분


def solution(k, score):
    hall = []
    answer = []

    for i in range(len(score)):
        if i < k:
            hall.append(score[i])
        else:
            if score[i] > min(hall):
                hall.remove(min(hall))
                hall.append(score[i])

        answer.append(min(hall))

    return answer


def solution(k, score):
    hall = []
    answer = []

    for s in score:
        hall.append(s)

        if len(hall) > k:
            hall.remove(min(hall))

        answer.append(min(hall))

    return answer


print(solution(3, [10, 100, 20, 150, 1, 100, 200]))

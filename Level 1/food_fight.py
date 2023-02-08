# 푸트 파이트 대회
# 풀이 시간 : 6분


def solution(food):
    answer = ""

    for i in range(1, len(food)):
        answer += (food[i]) // 2 * str(i)

    return answer + "0" + answer[::-1]

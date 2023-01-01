# 등수 매기기
from statistics import mean


def solution(score):
    average = [mean(s) for s in score]
    sorted_average = sorted(average, reverse=True)
    # index 함수에서 처음 발견된 index 기준이기 때문에 공동 등수는 알아서 체크 됨
    answer = [sorted_average.index(a) + 1 for a in average]

    return answer


solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]])

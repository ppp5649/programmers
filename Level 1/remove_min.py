# 제일 작은 수 제거하기
# 풀이 시간 : 5분


def solution(arr):
    arr.remove(min(arr))

    return arr or [-1]

# 행렬의 덧셈
# 풀이 시간 : 6분


def solution(arr1, arr2):
    return [[i + j for i, j in zip(x, y)] for x, y in zip(arr1, arr2)]

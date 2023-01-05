# # 가까운 수


# def solution(array, n):
#     min_difference = min([abs(n - item) for item in array])
#     answer = 0

#     if n + min_difference in array and n - min_difference in array:
#         answer += min(n + min_difference, n - min_difference)
#     elif n + min_difference in array:
#         answer += n + min_difference
#     else:
#         answer += n - min_difference

#     return answer


def solution(array, n):
    array.sort()
    difference = [abs(n - item) for item in array]

    return array[difference.index(min(difference))]


solution([21, 11, 12, 15, 14], 13)

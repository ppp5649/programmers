# 햄버거 만들기


def hamburger(ingredient):
    answer = 0
    len_check = []
    idx_check = 2

    while len(set(len_check)) == len(len_check):
        for idx in range(idx_check - 2, len(ingredient) - 3):
            if ingredient[idx : idx + 4] == [1, 2, 3, 1]:
                del ingredient[idx : idx + 4]
                answer += 1
                idx_check = idx
                break

        len_check.append(len(ingredient))

    return answer


# 재귀 함수 이용한 풀이 -> 시간 초과

# global answer
# answer= 0

# def hamburger(ingredient):
#     for idx in range(len(ingredient)-3):
#         if ingredient[idx:idx+4] == [1,2,3,1]:
#             del ingredient[idx:idx+4]
#             global answer
#             answer += 1
#             hamburger(ingredient)

#     return answer

# print(hamburger([2, 1, 1, 2, 3, 1, 2, 3, 1]))

# 모의고사
# 풀이 시간 : 40분


def solution(answers):
    arr1 = [1, 2, 3, 4, 5] * (len(answers) // 5)
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) // 5)
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // 10)

    b1 = [True if a == b else False for a, b in zip(arr1[0 : len(answers)], answers)]
    b2 = [True if a == b else False for a, b in zip(arr2[0 : len(answers)], answers)]
    b3 = [True if a == b else False for a, b in zip(arr3[0 : len(answers)], answers)]

    result = [sum(b1), sum(b2), sum(b3)]

    if result.count(max(result)) == 1:
        return [result.index(max(result)) + 1]
    # elif result.count(max(result)) == 2:
    #     result.
    else:
        return [1, 2, 3]


print(solution([1, 2, 3, 4, 5]))

tmp = [1, 2, 5]
st_tmp = sorted(tmp, reverse=True)
rank = {}
for i, n in enumerate(st_tmp):
    if n not in rank:
        rank[n] = i + 1

print(rank)

# 카드 뭉치
# 풀이 시간 : 8분


def solution(cards1, cards2, goal):
    idx1 = []
    idx2 = []

    for g in goal:
        if g in cards1:
            idx1.append(cards1.index(g))
        else:
            idx2.append(cards2.index(g))

    arr1 = [i for i in range(len(idx1))]
    arr2 = [i for i in range(len(idx2))]

    if idx1 == arr1 and idx2 == arr2:
        return "Yes"

    return "No"


solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])

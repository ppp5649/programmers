# 로또의 최고 순위와 최저 순위
# 풀이 시간 : 10분


def solution(lottos, win_nums):
    best = 0
    worst = 0
    rank = [6, 6, 5, 4, 3, 2, 1]

    for l in lottos:
        if l in win_nums:
            best += 1
            worst += 1
    best += lottos.count(0)

    return [rank[best], rank[worst]]


def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    best = len(set(lottos) & set(win_nums)) + lottos.count(0)
    worst = len(set(lottos) & set(win_nums))

    return [rank[best], rank[worst]]

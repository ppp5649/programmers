# 카펫
# 풀이 시간 : 40분


def solution(brown, yellow):
    total = int((brown + 4) / 2)

    for i in range(total - 3, 2, -1):
        for j in range(3, total - 2):
            if i >= j and i + j == total and i * j == brown + yellow:
                return [i, j]


# i >= j 조건 일때 이미 return값이 발생하기 때문에 굳이 조건 필요 X
# i+j 값은 total인 것을 알고 i는 정해졌으므로 j는 total - i로 고정
# 그러므로 2번째 조건도 필요없고 for문도 1개밖에 필요하지 않음


def solution(brown, yellow):
    total = int((brown + 4) / 2)

    for i in range(total - 3, 2, -1):
        if i * (total - i) == brown + yellow:
            return [i, total - i]

# 최솟값 만들기
# 풀이 시간 : 3분


# 작은 수는 큰 수와 곱해야 최소가 될 것 같아서 A는 오름차순 B는 내림차순으로 정렬 후 더해주었음


def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    return sum([a * b for a, b in zip(A, B)])

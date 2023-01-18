# 두 정수 사이의 합
# 풀이 시간 : 3분


def add_between(a, b):
    return sum(range(b, a + 1)) if a > b else sum(range(a, b + 1))


# 등차수열의 합 공식 이용 - O(1) 실행시간 0.00ms
def add_between(a, b):
    return (abs(a - b) + 1) * (a + b) // 2

# 부족한 금액 계산하기
# 풀이 시간 : 5분


def solution(price, money, count):
    lack = sum(range(1, count + 1)) * price - money

    return lack if lack > 0 else 0

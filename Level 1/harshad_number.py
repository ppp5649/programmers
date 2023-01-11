# 하샤드 수
# 풀이 시간 : 3분


def harshad_number(x):
    digits = sum(map(int, str(x)))

    return x % digits == 0

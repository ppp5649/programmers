# 자연수 뒤집어 배열로 만들기


def reverse_digits(n):
    return list(map(int, str(n)))[::-1]

# 저주의 숫자 3


def solution(n):
    cursed_numbers = ["x" if i % 3 == 0 or "3" in str(i) else i for i in range(1, 200)]

    while "x" in cursed_numbers:
        cursed_numbers.remove("x")

    return cursed_numbers[n - 1]


print(solution(100))

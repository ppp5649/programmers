# 콜라츠 추측
# 풀이 시간 : 10분
# num == 1일때 0으로 처리하는게 관건이었음


def solution(num):
    count = 0
    if num == 1:
        return 0

    else:
        while count < 500:
            count += 1
            num = num // 2 if num % 2 == 0 else 3 * num + 1

            if num == 1:
                return count

    return -1


def solution(num):
    for i in range(501):
        if num == 1:
            return i

        num = num // 2 if num % 2 == 0 else 3 * num + 1

    return -1

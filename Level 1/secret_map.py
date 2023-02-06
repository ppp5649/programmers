# 카카오 1차 비밀지도
# 풀이 시간 : 1시간

# 2진수 변환 직접 구현
from collections import deque


def solution(n, arr1, arr2):
    x_arr = [deque([]) for _ in range(len(arr1))]
    y_arr = [deque([]) for _ in range(len(arr2))]

    for i, x in enumerate(arr1):
        while x > 0:
            x_arr[i].appendleft(x % 2)
            x = x // 2

    for i, y in enumerate(arr2):
        while y > 0:
            y_arr[i].appendleft(y % 2)
            y = y // 2

    for x in x_arr:
        while len(x) < n:
            x.appendleft(0)

    for y in y_arr:
        while len(y) < n:
            y.appendleft(0)

    answer = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if x_arr[i][j] + y_arr[i][j] == 0:
                answer[i].append(" ")
            else:
                answer[i].append("#")
        answer[i] = "".join(answer[i])

    return answer


def solution(n, arr1, arr2):
    x_arr = [bin(x)[2:] for x in arr1]
    y_arr = [bin(y)[2:] for y in arr2]

    for i in range(n):
        x_arr[i] = "0" * (n - len(x_arr[i])) + x_arr[i]
        y_arr[i] = "0" * (n - len(y_arr[i])) + y_arr[i]

    answer = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if int(x_arr[i][j]) | int(y_arr[i][j]):
                answer[i].append("#")
            else:
                answer[i].append(" ")
        answer[i] = "".join(answer[i])

    return answer


# 10진수 -> 2진수 변환 bin 함수
# 10진수끼리 or 연산해도 논리연산 알아서 해서 2진수로 바꿔줌


def solution(n, arr1, arr2):
    answer = []
    for x, y in zip(arr1, arr2):
        a12 = str(bin(x | y))[2:]
        # 자릿수 맞춰주는 함수 rjust, ljust
        a12 = a12.rjust(n, "0")
        # replace 할 때 변수 재선언
        a12 = a12.replace("1", "#")
        a12 = a12.replace("0", " ")
        answer.append(a12)

    return answer


# solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])

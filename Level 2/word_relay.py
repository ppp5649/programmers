# 영어 끝말잇기
# 풀이 시간 : 50분

# import math


# def solution(n, words):
#     stack = []

#     for i in range(len(words) - 1):
#         if words[i] in stack:
#             return [n if (i + 1) % n == 0 else (i + 1) % n, math.ceil((i + 1) / n)]

#         if words[i][-1] != words[i + 1][0]:
#             return [n if (i + 2) % n == 0 else (i + 2) % n, math.ceil((i + 2) / n)]


#         stack.append(words[i])

#     if words[-1] in stack:
#         return [
#             n if len(words) % n == 0 else len(words) % n,
#             math.ceil(len(words) / n)
#         ]

#     return [0, 0]


# 숫자들의 반복을 몫과 나머지로 표현할 때 idx 자체, idx + 1을 n으로 나누었을 때 정수부와 소수부를 유심히 관찰하자 최대한 math 사용 안하고 가능한지 확인해보자

# range를 0 ~ len-1까지 잡으면 마지막 인덱스가 비고 1 ~ len까지 잡으면 첫번째 인덱스가 빈다. 문제 조건에 맞게 유동적으로 사용하자


def solution(n, words):
    stack = [words[0]]

    for i in range(1, len(words)):
        if words[i] in stack or words[i][0] != words[i - 1][-1]:
            return [i % n + 1, i // n + 1]

        stack.append(words[i])

    return [0, 0]

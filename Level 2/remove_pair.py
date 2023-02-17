# 짝지어 제거하기
# 풀이 시간 : 30분

# # 효율성 0 정확성 70
# def solution(s):
#     check_len = [0]

#     while check_len[-1] != len(s):
#         check_len.append(len(s))
#         for i in range(len(s) - 1):
#             if s[i] == s[i + 1]:
#                 s = s.replace(s[i], "", 2)
#                 break

#     if len(s) == 0:
#         return 1
#     else:
#         return 0


def solution(s):
    answer = 0
    stack = []

    for c in s:
        if len(stack) == 0:
            stack.append(c)

        else:
            if c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

    if len(stack) == 0:
        answer = 1

    return answer

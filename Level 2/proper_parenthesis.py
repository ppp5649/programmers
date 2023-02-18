# 올바른 괄호
# 풀이 시간 : 2시간 (못품)


# def solution(s):
#     answer = []
#     if s[0] == ")":
#         return False

#     else:
#         for i in range(len(s)):
#             if s[i] == ")":
#                 answer.append(s[:i])
#     print(answer)
#     return True


def solution(s):
    stack = []

    if s[0] == ")" or s.count("(") != s.count(")"):
        return False

    else:
        for c in s:
            stack.append(c)
            if stack[-1] == "(" and stack.count(")") != 0:
                if stack[:-1].count("(") != stack[:-1].count(")"):
                    return False
                else:
                    del stack[:-1]

    return True


def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif not stack or stack.pop() != "(":
            return False
    return False if stack else True


print(solution("(())"))

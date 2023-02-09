# 올바른 괄호
# 풀이 시간 : 50분 (아직 풀지 못함)


def solution(s):
    answer = []
    if s[0] == ")":
        return False

    else:
        for i in range(len(s)):
            if s[i] == ")":
                answer.append(s[:i])
    print(answer)
    return True


solution("(())())")

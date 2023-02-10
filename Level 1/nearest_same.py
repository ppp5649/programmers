# 가장 가까운 같은 글자
# 풀이 시간 : 15분


def solution(s):
    answer = []

    for i in range(len(s)):
        if s[:i].find(s[i]) == -1:
            answer.append(-1)
        else:
            for j in range(i - 1, -1, -1):
                if s[j] == s[i]:
                    answer.append(i - j)
                    break

    return answer


def solution(s):
    answer = []
    dic = {}

    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])

        dic[s[i]] = i

    return answer

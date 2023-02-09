# JadenCase 문자열 만들기
# 풀이 시간 : 12분

# 처음에 split()으로 쪼개서 공백 기준으로 문자열을 더해주었는데 중간에 공백이 여러개 들어가 있는 경우 예외 발생

# 이전 문자가 공백인 경우 그 다음 문자는 대문자 그 외에는 소문자로 answer에 더해주고 맨 첫 문자가 빠지므로 answer을 처음부터 s[0].upper()로 시작


def solution(s):
    answer = f"{s[0].upper()}"

    for i in range(len(s) - 1):
        if s[i] == " ":
            answer += s[i + 1].upper()
        else:
            answer += s[i + 1].lower()

    return answer

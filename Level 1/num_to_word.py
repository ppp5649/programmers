# 2021 카카오 인턴십 > 숫자 문자열과 영단어
# 풀이 시간 : 7분


def solution(s):
    num_dic = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for key, value in num_dic.items():
        s = s.replace(key, value)

    return int(s)


# 리스트로 푼 경우 (index와 숫자가 자동으로 맞아 떨어지므로)
def solution(s):
    word = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    for i, n in enumerate(word):
        s = s.replace(n, str(i))

    return int(s)

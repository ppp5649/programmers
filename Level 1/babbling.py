# 옹알이 (2)
def solution(babbling):
    answer = 0
    can_dict = {"aya": "!", "ye": "@", "woo": "#", "ma": "$"}
    cleaned_list = []

    for b in babbling:
        for k, v in can_dict.items():
            b = b.replace(k, v)

        cleaned_list.append(b)
        print(b)

        for idx in range(len(b) - 1):
            if b[idx] == b[idx + 1]:
                if b in cleaned_list:
                    cleaned_list.remove(b)

    for element in cleaned_list:
        for s in "!@#$":
            element = element.replace(s, "")
        if element == "":
            answer += 1

    return answer


# solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])

# 정환이가 푼 답
from copy import deepcopy


def solution(babbling):

    can_babbling = ["aya", "ye", "woo", "ma"]
    answer = 0
    for word in babbling:
        org_word = deepcopy(word)
        for can_word in can_babbling:
            rep_word = org_word.replace(can_word, "*")
            if "**" not in rep_word:
                word = word.replace(can_word, "*")
        word = word.replace("*", "")
        answer += 1 if len(word) == 0 else 0

    return answer


# solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])

# 2월 28일 다시 풀어봄

# %%
def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    replace = "@#$%"
    check = []

    for i in range(len(babbling)):
        for j in range(4):
            babbling[i] = babbling[i].replace(can[j], replace[j])

    for i in range(len(babbling)):
        for j in range(len(babbling[i]) - 1):
            if babbling[i][j] == babbling[i][j + 1]:
                check.append(i)
                break

    for i in range(len(babbling)):
        for re in replace:
            babbling[i] = babbling[i].replace(re, "")

    for i in range(len(babbling)):
        if babbling[i] != "":
            check.append(i)

    return len(babbling) - len(set(check))


solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])

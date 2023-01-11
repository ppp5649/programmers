### 2022 KAKAO TECH INTERNSHIP > 성격 유형 검사하기 ###

# # sol 1

# # initial score
# r_score = 0
# t_score = 0
# c_score = 0
# f_score = 0
# j_score = 0
# m_score = 0
# a_score = 0
# n_score = 0

# # dictionary - type : score
# score_dict = {"R":r_score, "T":t_score, "C":c_score, "F":f_score, "J":j_score, "M":m_score, "A":a_score, "N":n_score}

# # the type score minus to another type score plus
# val_dict = {1:3, 2:2, 3:1, 4:0, 5:-1, 6:-2, 7:-3}

# # before list(choiced) to string(answer)
# choiced = []

# def kakao_mbti(survey, choices):
#     # calculate score
#     for pair in zip(survey, choices):
#         if pair[1] in list(val_dict.keys()):
#             score_dict[pair[0][0]] += val_dict[pair[1]]


#     # devide k,v for comparing types
#     type_list = list(score_dict.keys())
#     score_list = list(score_dict.values())

#     # use even, odd for comparing types
#     for i in range(0,8,2):
#         if score_list[i] > score_list[i+1]:
#             choiced.append(type_list[i])

#         elif score_list[i] < score_list[i+1]:
#             choiced.append(type_list[i+1])

#         else :
#             choiced.append(sorted([type_list[i],type_list[i+1]])[0])

#     # list to string
#     answer = "".join(choiced)

#     return answer

# sol 2


def kakao_mbti(survey, choices):
    answer = ""

    scores = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    add_score = {1: 3, 2: 2, 3: 1, 4: 0, 5: -1, 6: -2, 7: -3}

    for i in range(len(survey)):
        scores[survey[i][0]] += add_score[choices[i]]

    # use >= for sorting
    answer += "R" if scores["R"] >= scores["T"] else "T"
    answer += "C" if scores["C"] >= scores["F"] else "F"
    answer += "J" if scores["J"] >= scores["M"] else "M"
    answer += "A" if scores["A"] >= scores["N"] else "N"

    return answer

# 완주하지 못한 선수
# Counter 직접 구현해서 다시 풀어보기
from collections import Counter


def marathon(participant, completion):

    p_dict = Counter(participant)
    c_dict = Counter(completion)

    for p_name in p_dict:
        if p_dict[p_name] != c_dict[p_name]:
            answer = p_name

    return answer

    # for문을 이용한 counter
    # for man in participant:
    #     if man not in man_dict:
    #         man_dict[man] = 1
    #     else:
    #         man_dict[man] += 1

    # 파이썬 내장 Counter 함수
    # participant = Counter(participant)


# participant에 동명이인이 있는 경우 - 동명이인이 answer
# 동명이인이 없는 경우 - completion에 없는 participant가 answer

# 내 풀이 - 예외케이스도 못잡아내고 속도도 느림
# def marathon(participant, completion):
#     answer = ''
#     # 동명이인이 존재하는 경우
#     if len(participant) != len(set(participant)):
#         sorted_p = sorted(participant)
#         for idx in range(len(sorted_p)-1):
#             if sorted_p[idx] == sorted_p[idx+1]:
#                 answer = sorted_p[idx]


#     # 반대 경우
#     else :
#         # set의 집합 연산 이용
#         answer = list(set(participant) - set(completion))[0]

#         # 수정 전 코드
#         # for p in participant:
#         #     if p not in completion:
#         #         answer = p

#     return answer

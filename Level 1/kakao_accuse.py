# 카카오 2022 신고 결과 받기
# 풀이 시간 : 90분

from collections import Counter


def solution(id_list, report, k):
    # report 중복 제거(1회 처리) 후 신고자와 피신고자를 튜플로 생성
    accuse = [(r.split(" ")[0], r.split(" ")[1]) for r in set(report)]
    accused = [a[1] for a in accuse]
    # blocked에서 시간초과
    # 기존에는 for ed in accused 로 접근했고 아래 코드로 탐색 수를 줄임
    blocked = [key for key, value in Counter(accused).items() if value >= k]
    count = {i: 0 for i in id_list}

    # 신고 메일 받은 횟수 더하기
    for a in accuse:
        if a[1] in blocked:
            count[a[0]] += 1

    answer = [count[i] for i in id_list]

    return answer


# 과거에 접근했던 과정 - 똥인지 된장인지도 몰랐을 때 함수 자체를 이해못했었네

# def solution(id_list, report, k):
#     id_list = ['muzi', 'apeach','frodo','neo' ]
#     report = []
#     for idx in range(len(id_list)):
#         report.append(id_list[idx])
#     print(report)
#     answer = []

#     return answer

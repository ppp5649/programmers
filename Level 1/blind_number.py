# 핸드폰 번호 가리기
# 풀이 시간 : 3분


def solution(phone_number):
    std = len(phone_number) - 4
    return "*" * std + phone_number[std:]

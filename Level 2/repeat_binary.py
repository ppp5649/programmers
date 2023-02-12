# 이진 변환 반복하기
# 풀이 시간 : 10분

# 지금까지 for문 돌려서 이상하게 replace() 함수를 사용했던 것 같다.
# replace()의 3번째 파라미터는 치환 횟수인데 횟수를 입력하지 않으면 문자열 내 첫번째 파라미터인 모든 문자를 치환한다.


def binary(s):
    s = s.replace("0", "")

    return bin(len(s))[2:]


def solution(s):
    answer = [0, 0]

    while s != "1":
        answer[1] += s.count("0")
        s = binary(s)
        answer[0] += 1

    return answer


# s = "10101"
# print(s.replace("0", ""))  # "0"이 제거된 "111"이라는 새로운 객체

# print(s)  # "10101"
# print(id(s))  # 변수 s가 가리키는 객체는 변하지 않음

# # s 자체를 변경하려면 재선언이 필요하다.
# s = s.replace("0", "")
# print(s)  # "111"
# print(id(s))  # 변수 s는 새로운 객체를 가리킴

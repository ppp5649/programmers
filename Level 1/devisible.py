# 나누어 떨어지는 숫자 배열
# 풀이 시간 : 4분


def solution(arr, divisor):
    answer = sorted([num for num in arr if num % divisor == 0])
    if answer == []:
        return [-1]

    return answer


# 논리연산자 or을 이용한 풀이 (빈 리스트는 bool값이 False)


def solution(arr, divisor):
    return sorted([num for num in arr if num % divisor == 0]) or [-1]

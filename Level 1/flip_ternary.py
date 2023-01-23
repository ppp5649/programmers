# 3진법 뒤집기
# 풀이 시간 : 20분


def solution(n):
    digits = 0
    base_3 = ""
    answer = 0

    # 자릿수 구하기
    while n // (3**digits) > 0:
        digits += 1

    # 각 자릿수 구하기
    while digits > 0:
        digits -= 1
        base_3 += str(n // (3**digits))
        n = n % (3**digits)

    # index를 0부터 시작하면 자연스럽게 뒤집어서 자릿수 정해짐
    for i in range(len(base_3)):
        answer += int(base_3[i]) * (3**i)

    return answer


# 몫과 나머지로 진법 변환, while n, int 함수로 10진법 변환 배울점 많은 코드
def solution(n):
    ternary = ""

    while n:
        ternary += str(n % 3)
        n = n // 3

    return int(ternary, 3)

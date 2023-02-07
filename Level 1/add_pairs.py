# 두 개 뽑아서 더하기
# 풀이 시간 : 6분

from itertools import combinations


def solution(numbers):
    c_num = combinations(numbers, 2)
    answer = [c[0] + c[1] for c in c_num]

    # sorted 함수는 iterable한 객체를 매개변수로 받고
    # 결과는 list로 반환하기 때문에 굳이 list 함수를 쓸 필요 X
    return sorted(set(answer))


def solution(numbers):
    answer = []

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    return sorted(set(answer))


def solution(numbers):
    n = numbers
    answer = [n[i] + n[j] for i in range(len(n)) for j in range(len(n)) if i < j]

    return sorted(set(answer))

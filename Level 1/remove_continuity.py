# 같은 숫자는 싫어
# 풀이 시간 : 7분


def solution(arr):
    new_arr = [arr[0]]

    for a in arr:
        if new_arr[-1] != a:
            new_arr.append(a)

    return new_arr


# 슬라이싱을 이용하여 인덱스 에러를 피하는 방법
def solution(arr):
    new_arr = []

    for a in arr:
        if new_arr[-1:] != [a]:
            new_arr.append(a)

    return new_arr

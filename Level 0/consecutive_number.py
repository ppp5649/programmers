def solution(num, total):
    # 등차수열의 합 공식을 이용하여 첫째항을 구함 (공차는 1)
    a1 = int((total / num) - ((num - 1) / 2))

    return [i for i in range(a1, a1 + num)]


print(solution(5, 5))

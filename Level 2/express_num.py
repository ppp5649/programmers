# 숫자의 표현
# 풀이 시간 : 45분 + 힌트보고 불필요한 탐색 제거


def solution(n):
    n_arr = [i + 1 for i in range(n)]
    answer = 0

    for i in range(n):
        for j in range(i + 1, n + 1):
            if sum(n_arr[i:j]) == n:
                answer += 1
                break
            # 이미 합이 n을 넘어가는 경우 굳이 더 탐색할 필요가 없으므로 break
            elif sum(n_arr[i:j]) > n:
                break

    return answer


# n이 연속된 수의 합이 되려면
# 1. 항의 개수가 짝수 일때 ... k k+1  ... 이므로 n = (2k+1)*m 형태로 표현 가능
# 이때 2k+1은 n의 홀수인 약수
# 2. 항의 개수가 홀수 일때 .. 가장 가운데 k 기준으로 k-1과 k+1이 짝이 되므로
# n = 2kl + k = (2l+1)*k 이때 2l+1은 n의 홀수인 약수

# 홀수인 약수의 개수 구하기


def solution(n):
    answer = []

    for i in range(1, (n // 2) + 1):
        if n % i == 0 and i % 2 != 0:
            answer.append(i)

    if n % 2 != 0:
        answer.append(n)

    return len(answer)


solution(15)

# 등차수열의 합 / k를 빼서 나누어 떨어지는지 확인하는 알고리즘(O(n**0.5)) 공부하기

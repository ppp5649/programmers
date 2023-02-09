# 소수 찾기
# 풀이 시간 : 1시간


# 소수인지 아닌지 판별하는 경우에는 1과 자기자신을 제외한 약수가 한 개라도 존재하는지 확인하면 된다.

# 최대한 시간 복잡도를 줄이기 위해 제곱근 N까지만 확인하면 되는데 그 이유는
# N = A X B 라고 가정했을 때 제곱수가 아니라면 A와 B중 작은 수는 항상 제곱근 N 보다 작다. 제곱근 N까지 탐색했을 때 약수가 없다면 그 이후에도 약수는 존재하지 않는다. 약수는 제곱근 N 기준 대칭이기 때문이다.(시간 복잡도 O(N) -> O(N^1/2))


def is_prime(k):
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            return False

    return True


def solution(n):
    answer = 0
    for i in range(2, n + 1):
        answer += is_prime(i)

    return answer


# 에라토스테네스의 체 (시간복잡도는 낮지만 메모리가 N만큼 소모되기 때문에 N이 100만 이하일 때 추천)
# 위 코드 보다 10배 빠름


def cnt_prime(n):
    arr = [True] * (n + 1)

    for i in range(2, int(n**0.5) + 1):
        if arr[i] == True:  # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                arr[i * j] = False
                j += 1

    return len([i for i in range(2, n + 1) if arr[i]])

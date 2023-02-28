# 유한소수 판별하기

# 우선 a와 b의 최대공약수를 구해야 기약분수로 나타낼 수 있음
# 기약분수의 분모가 소인수로 2와 5만 가져야 유한소수 그 외에는 무한소수
# 소인수의 정의 : 약수 중에서 소수인 약수

# Solution 1 - 최대공약수, 소인수 직접 구함


def get_prime_factor(n):
    # 1을 제외한 약수
    divisor = [i for i in range(2, n + 1) if n % i == 0]
    prime_number = []
    prime_factor = []

    for d in divisor:
        for i in range(1, d + 1):
            if d % i == 0:
                prime_number.append(i)
        if len(prime_number) == 2:
            prime_factor.append(d)
        prime_number.clear()

    return prime_factor


def solution(a, b):
    gcd = 0

    # 최대공약수 - 연산량이 적어서 리스트에서 max 구하는 것보다 빠름
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            gcd += i
            break

    b = int(b / gcd)
    prime_factor = get_prime_factor(b)

    tmp = [2, 5]

    for t in tmp:
        if t in prime_factor:
            prime_factor.remove(t)

    if len(prime_factor) == 0:
        return 1

    return 2


# solution 2
def solution(a, b):
    gcd = max([i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0])
    b = b / gcd

    while b % 2 == 0:
        b //= 2

    while b % 5 == 0:
        b //= 5

    return 1 if b == 1 else 2

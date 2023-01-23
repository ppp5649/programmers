# 최대공약수와 최소공배수
# 풀이 시간 : 3분

# 코드는 간결하지만 속도 매우 느림
def solution(n, m):
    # gcd 구할 때 역순으로 탐색하는 것이 핵심
    gcd = max([i for i in range(min(n, m), 0, -1) if n % i == 0 and m % i == 0])
    lcm = min([i for i in range(max(n, m), n * m + 1) if i % n == 0 and i % m == 0])

    return [gcd, lcm]


# 정석대로 구했을 때 그나마 속도 빠른 편
def solution(n, m):
    gcd = 0
    lcm = 0

    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            gcd += i
            break

    for j in range(max(n, m), n * m + 1):
        if j % n == 0 and j % m == 0:
            lcm += j
            break

    return [gcd, lcm]


# 유클리드 호제법 (몫과 나머지로 최대공약수 구하는 방법)
def solution(n, m):
    a, b = max(n, m), min(n, m)

    while b > 0:
        a, b = b, a % b

    gcd = a
    lcm = n * m / gcd

    return [gcd, lcm]


print(solution(3, 12))

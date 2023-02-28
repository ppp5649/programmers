# 기사단원의 무기
# 풀이 시간 : 22분

# 약수의 개수 구하는 최적의 알고리즘
# 임의의 자연수 N의 약수들 중에서 두 약수의 곱이 N이 되는 약수 A(i)와 약수 B(n//i)
# 는 반드시 존재하므로 다음과 같이 개수를 구하면 된다.

# 1 ~ 제곱근 n까지의 약수의 개수를 더하고 그 중에 짝이 되는 약수 A와 B가 같을 때
# 즉, 제곱수 일때를 제외하고 하나씩 추가로 더해준다.


def cnt_divisor(n):
    cnt = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            cnt += 1
            if i != (n // i):
                cnt += 1

    return cnt


def solution(number, limit, power):
    answer = 0
    cnt_arr = [cnt_divisor(i) for i in range(1, number + 1)]

    for c in cnt_arr:
        if c > limit:
            answer += power

        else:
            answer += c

    return answer


solution(5, 3, 2)

def solution(denum1, num1, denum2, num2):
    # 통분 후 덧셈(단순히 분모의 곱)
    num = num1 * num2
    denum = denum1 * num2 + denum2 * num1

    # 덧셈 한 결과 기약분수로 나타내기(최대공약수로 나누기)
    gcd = max(
        [i for i in range(1, min(num, denum) + 1) if num % i == 0 and denum % i == 0]
    )
    num, denum = int(num / gcd), int(denum / gcd)

    return [denum, num]


solution(1, 2, 3, 4)

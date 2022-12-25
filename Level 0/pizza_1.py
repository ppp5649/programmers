# 피자 나눠 먹기 (1)

def solution(n):
    for i in range(100//7+1):
        if i*7 < n < (i+1)*7+1:
            answer = i+1

    return answer

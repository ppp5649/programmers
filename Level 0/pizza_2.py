# 피자 나눠 먹기 (2)
# 최소공배수 구하는게 관건 - 오바라고 생각 n<= 100이니까
# if break문을 사용하면 조건이 만족했을경우 반복문을 빠져나간다. 매우 유용할듯

def solution(n):
    i = 0
    
    while True:
        i += 6
        if i%n == 0:
            answer = i/6
            break
    
    return answer



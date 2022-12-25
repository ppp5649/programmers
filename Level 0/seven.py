# 7의 개수 구하기 - 숫자로 직접 나누고 지지고 볶고 하는 문제가 아님
# 핵심은 str으로 바꾸는 것

def solution(array):
    array = "".join(list(map(str,array)))
    answer = array.count("7")
        
    return answer


# # 삼각형의 결정조건 (1)

def solution(sides):
    sides.sort()
    
    if sides[2] < sides[0] + sides[1]:
        answer = 1
    else:
        answer = 2

    return answer

print(solution([3,6,2]))

# 좋은 풀이

def solution(sides):
    answer = 1 if max(sides) < (sum(sides)-max(sides)) else 2
    return answer
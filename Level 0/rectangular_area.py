# 직사각형의 넓이 구하기

# x축 좌표가 같은 경우 max에서 min을 뺀 길이 = 밑변
# y축 좌표가 같은 경우 max에서 min을 뺀 길이 = 높이

def solution(dots):
    x_dot = [dot[0] for dot in dots]
    y_dot = [dot[1] for dot in dots]
    answer = (max(x_dot) - min(x_dot)) * (max(y_dot) - min(y_dot))
    
    return answer

solution([[1, 1], [2, 1], [2, 2], [1, 2]])
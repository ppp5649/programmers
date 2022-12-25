# LV.0 평행
def solution(dots):

    slide = []
    result = 0
    for i in range(0,3):
        for j in range(i+1,4):
            slide.append((dots[i][0] - dots[j][0]) / (dots[i][1] - dots[j][1])) 
    
    if len(slide) == len(set(slide)):
        result = 0
    
    else:
        result = 1
    
    print(slide)
    print(list(set(slide)))
    
    return result

solution([[1, 4], [9, 2], [3, 8], [11, 6]])
# 01 02 03 / 12 13 / 23 이런식으로 갯수가 증가하거나 감소하면서 탐색하는 경우
# Bubble Sort를 사용하면 된다. 이중 for문 사용하고 i로 갯수 조절
# set 함수는 기존 순서가 유지되지 않는 특성을 몰라서 len없이 비교했는데 틀렸음

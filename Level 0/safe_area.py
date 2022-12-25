# 안전지대
from copy import deepcopy

def solution(matrix):
# 지뢰가 있는지역과 주위 위험지역을 구분하기 위해 지뢰를 2로 변경
    for column in range(len(matrix)):
        for row in range(len(matrix)):
            if matrix[column][row] == 1:
                matrix[column][row] = 2
    # 2행 2열씩 확장시켜 range over가 일어나지 않도록 extended_matrix 생성
    extended_matrix = [["m"]*(len(matrix)+2) for i in range(len(matrix)+2)]
    
    # 새로 확장된 지역의 값은 모두 1로 안전지대 갯수 카운트에 영향 X
    for column in range(len(matrix)+2):
        for row in range(len(matrix)+2):
            if 1 <= column <= len(matrix) and 1 <= row <= len(matrix):
                extended_matrix[column][row] = matrix[column-1][row-1]
            else :
                extended_matrix[column][row] = 1
    # 아래 for문에서 2 -> 1로 바뀌면서 폭탄이 인식되지 않는 경우 대비하여 deepcopy
    copyed = deepcopy(extended_matrix)

    # range over가 일어나지 않기 때문에 주위 8개 위험지역 1로 매핑
    for column in range(len(matrix)+2):
        for row in range(len(matrix)+2):
            if 1 <= column <= len(matrix) and 1 <= row <= len(matrix):
                if copyed[column][row] == 2:
                    extended_matrix[column-1][row-1] = 1
                    extended_matrix[column][row-1] = 1
                    extended_matrix[column+1][row-1] = 1
                    extended_matrix[column-1][row] = 1
                    extended_matrix[column+1][row] = 1
                    extended_matrix[column-1][row+1] = 1
                    extended_matrix[column][row+1] = 1
                    extended_matrix[column+1][row+1] = 1
                    
            else:
                extended_matrix[column][row] = 1 

    return zero_counter(extended_matrix)

# 안전지대인 0값의 개수를 출력하는 함수
def zero_counter(matrix):
    count = 0
    for column in range(len(matrix)):
        for row in range(len(matrix)):
            if matrix[column][row] == 0:
                count += 1
    
    return count
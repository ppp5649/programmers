# 최소 직사각형
# 풀이 시간 : 30분 풀고 포기하고 정답 확인


# 가로 세로 중 긴 것들은 한쪽에 몰아넣고 작은 것들도 한쪽에 몰아넣으면 됨
# 그림으로 생각하면 편함
def solution(sizes):
    row = []
    col = []
    for i in range(len(sizes)):
        row.append(max(sizes[i]))
        col.append(min(sizes[i]))

    answer = max(row) * max(col)
    return answer


solution([[60, 50], [30, 70], [60, 30], [80, 40]])

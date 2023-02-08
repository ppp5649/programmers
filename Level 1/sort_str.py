# 문자열 내 마음대로 정렬하기
# 풀이 시간 : 1시간


def solution(strings, n):
    # 일단 사전순으로 정렬
    ss = sorted(strings)

    # Bubble Sort 이용하여 인덱스 n 기준으로 정렬
    for i in range(len(ss) - 1):
        for j in range(len(ss) - 1 - i):
            if ss[j][n] > ss[j + 1][n]:
                ss[j], ss[j + 1] = ss[j + 1], ss[j]

    return ss


# key값에 lambda 함수를 사용하여 정렬한 방법 (key값엔 함수가 들어감)
# 매개변수 x에는 비교대상인 strings의 요소들이 들어가고
# 그 요소가 s라고 했을때 s[i][n]과 s[i+k][n]이 비교되어 정렬되는 것
def solution(strings, n):
    strings.sort()
    return sorted(strings, key=lambda x: x[n])

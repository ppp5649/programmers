# 최댓값과 최솟값
# 풀이 시간 : 6분


def solution(s):
    arr = list(map(int, s.split()))
    mn_mx = [str(min(arr)), str(max(arr))]
    answer = " ".join(mn_mx)

    return answer


# 문자열 덧셈 이용해서 좀 더 간단하게 풀이
def solution(s):
    arr = list(map(int, s.split()))

    return str(min(arr)) + " " + str(max(arr))

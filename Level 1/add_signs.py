# 음양 더하기
# 풀이 시간 : 9분


def solution(absolutes, signs):
    return sum([absolutes[i] if signs[i] else -absolutes[i] for i in range(len(signs))])


# 두 리스트가 길이가 같다면 zip을 활용
def solution(absolutes, signs):
    return sum([a if s else -a for a, s in zip(absolutes, signs)])

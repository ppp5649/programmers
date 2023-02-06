# 문자열 내 마음대로 정렬하기
# 풀이 시간 : 30분 +


def solution(strings, n):
    nth = [s[n] for s in strings]
    st_nth = sorted(nth)
    rank = [st_nth.index(c) for c in nth]
    print(rank)
    # rank_dict = {r: s for s, r in zip(strings, rank)}

    # for i in range(len(strings)):
    #     strings[i] = rank_dict[i]

    return strings


solution(["abce", "abcd", "cdx"], 2)

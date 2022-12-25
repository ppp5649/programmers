# 배열의 유사도
# Set 자료구조의 교집합 활용 -> Set 자료구조 활용 많이 해보기

def solution(s1, s2):
    return len(set(s1)&set(s2))
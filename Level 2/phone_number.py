# 전화번호 목록 (해시)
# 풀이 시간 : 15분 (91.7 - 시간 초과) +
# 어떤 번호가 다른 번호의 접두어 일때니까 길이가 긴 것만 탐색하면 됨

# 시간 초과 코드
def solution(book):
    for idx in range(len(book)):
        for num in book:
            if len(book[idx]) < len(num):
                if book[idx] == num[: len(book[idx])]:
                    return False

    return True


# 해시를 이용해서 시간복잡도를 줄여보자
def solution(book):
    book_dict = {}
    answer = True
    return answer

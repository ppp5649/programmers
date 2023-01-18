# 전화번호 목록 (해시)
# 풀이 시간 : 15분 (91.7 - 시간 초과) +
# 어떤 번호가 다른 번호의 접두어 일때니까 길이가 긴 것만 탐색하면 됨

# # 시간 초과 코드
# def solution(book):
#     for idx in range(len(book)):
#         for num in book:
#             if len(book[idx]) < len(num):
#                 if book[idx] == num[: len(book[idx])]:
#                     return False

#     return True


# 해시를 안 쓴 최선


def solution(book):
    book.sort(key=len)
    for i in range(len(book)):
        for j in range(i + 1, len(book)):
            if book[i] == book[j][: len(book[i])]:
                return False

    return True


def solution(book):
    len_dict = {num: [] for num in book}
    for num in book:
        for keys in len_dict:
            if len(num) > len(keys):
                len_dict[keys].append(num)

    for k, v in len_dict.items():
        for tmp in v:
            if k in tmp:
                if k == tmp[: len(k)]:
                    return False

    return True


solution(["119", "117", "97674223", "1195524421"])

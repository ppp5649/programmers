# 서울에서 김서방 찾기
# 풀이 시간 : 2분


def solution(seoul):
    for idx in range(len(seoul)):
        if seoul[idx] == "Kim":
            return f"김서방은 {idx}에 있다"


def solution(seoul):
    location = seoul.index("Kim")
    return f"김서방은 {location}에 있다"

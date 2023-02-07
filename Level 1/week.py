# 2016년 (요일 구하기)
# 풀이 시간 : 20분


def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cnt_month = sum(days[: a - 1])
    day_dic = {1: "FRI", 2: "SAT", 3: "SUN", 4: "MON", 5: "TUE", 6: "WED", 0: "THU"}

    return day_dic[(cnt_month + b) % 7]


def solution(a, b):
    # 연도별 시작 요일에 따라 YEAR_IDX만 바꿔주면 됨
    YEAR_IDX = 5
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    cnt_days = sum(days[: a - 1]) + b - 1 + YEAR_IDX

    return week[(cnt_days) % 7]


# datetime 라이브러리 활용
import datetime


def solution(a, b):
    days = "MON TUE WED THU FRI SAT SUN".split()
    day_idx = datetime.date(2016, a, b).weekday()

    return days[day_idx]

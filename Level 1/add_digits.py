# 자릿수 더하기
# str도 iterable한 자료구조이므로 map 함수를 활용할 수 있고
# map object 자체는 print가 안되지만 interable 하므로 sum을 구하는데는 상관 X 굳이 list 씌울 필요 X


def add_digits(n):
    return sum(map(int, str(n)))

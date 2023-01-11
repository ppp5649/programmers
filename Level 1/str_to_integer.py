# 문자열을 정수로 바꾸기


def str_to_integer(s):
    try:
        return int(s)

    except ValueError:
        return -int(s[1:])


# -가 포함된 문자열은 int 함수 적용이 안되는 줄 알았는데 됨


def str_to_integer(s):
    return int(s)

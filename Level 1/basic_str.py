# 문자열 다루기 기본


def basic_str(s):
    if len(s) != 4 and len(s) != 6:
        return False

    else:
        try:
            int(s)

        except ValueError:
            return False

    return True


# try except 구문
# try에서 코드를 실행했을 때 에러가 뜨면 except 구문으로 넘어감
# 이때 특정 에러일때만 except로 넘어가도록 뒤에 Error를 지정 해줄수있음
# 굳이 문자열 요소를 돌지않고 문자열 그대로 int 씌워도 되는걸 간과함

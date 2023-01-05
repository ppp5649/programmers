# 다항식 더하기


def solution(polynomial):
    answer = ""
    terms = polynomial.split(" + ")
    first_term = 0
    linear_term = 0

    for i in range(len(terms)):
        if terms[i] == "x":
            terms[i] = "1x"
        x_idx = terms[i].find("x")
        if x_idx == -1:
            linear_term += int(terms[i])
        else:
            first_term += int(terms[i][0:x_idx])

    if first_term == 0 and linear_term == 0:
        answer = "0"
    elif first_term == 0:
        answer = f"{linear_term}"
    elif linear_term == 0:
        answer = "x" if first_term == 1 else f"{first_term}x"
    else:
        answer = (
            f"x + {linear_term}"
            if first_term == 1
            else f"{first_term}x + {linear_term}"
        )

    return answer


print(solution("x"))

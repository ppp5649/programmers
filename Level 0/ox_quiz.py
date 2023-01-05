def solution(quiz):
    answer = []

    for q in quiz:
        item = q.split(" ")

        if item[1] == "+":
            if int(item[0]) + int(item[2]) == int(item[4]):
                answer.append("O")
            else:
                answer.append("X")

        else:
            if int(item[0]) - int(item[2]) == int(item[4]):
                answer.append("O")
            else:
                answer.append("X")

    return answer


answer = []
quiz = ["-43 - 41 = -84", "-14 + 55 = 32"]

for q in quiz:
    item = q.split(" ")
    if item[1] == "+":
        if int(item[0]) + int(item[2]) == int(item[4]):
            answer.append("O")
        else:
            answer.append("X")

    else:
        if int(item[0]) - int(item[2]) == int(item[4]):
            answer.append("O")
        else:
            answer.append("X")
print(answer)

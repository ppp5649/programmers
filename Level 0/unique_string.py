def solution(my_string):
    # string도 iterable한 객체이기 때문에 dict.fromkeys() 함수 사용 가능
    # list 함수안에는 iterable 객체가 들어갈 수 있고 문자열 또한 가능 1글자씩 쪼개짐
    # my_list = list(my_string) 
    unique_list = list(dict.fromkeys(my_string)) 
    answer = "".join(unique_list)

    return answer
        
    

print(solution("people"))
# 컨트롤 Z

def solution(s):
    answer = 0
    dummy = 0
    s_list = s.split()

    # Z와 앞의 숫자 제거 과정 (out of index 대비하여 원본 유지)
    for idx in range(1, len(s_list)):
        if s_list[idx] == "Z":
            dummy += int(s_list[idx-1])
    
    for s in s_list:
        if s == "Z":
            s_list.remove("Z")

    num_list = list(map(int, s_list))
    
    for num in num_list:
        answer += num 

    answer = answer - dummy
    return answer

# 좋은 solution

def solution(s):
    arr = s.split()
    result =[]
    
    for i in arr :
        if i=='Z':
            result.pop()
        else:
            result.append(int(i))
    
    return sum(result)
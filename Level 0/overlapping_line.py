# 겹치는 선분의 길이

# 겹치는 선분의 길이 모두 더하라는 줄 알고 잘못 풀음 ..
# 문제 제대로 읽자 제발

def solution(lines):
    answer = 0
    for i in range(0,2):
        for j in range(1+i,3):
            f_len = (lines[i][1]-lines[i][0])
            b_len = (lines[j][1]-lines[j][0])
            max_dot = max(lines[i][0],lines[i][1],lines[j][0],lines[j][1])
            min_dot = min(lines[i][0],lines[i][1],lines[j][0],lines[j][1])
            
            if (max_dot - min_dot) >= (b_len + f_len):
                answer += 0
                
            else :
                answer += (b_len + f_len) - (max_dot - min_dot)

    return answer

from collections import Counter

def solution(lines):
    answer = 0

    last_dot = max(lines[0][1],lines[1][1],lines[2][1])
    first_dot = min(lines[0][0],lines[1][0],lines[2][0])
    
    f_sector = [[i,i+1] for i in range(lines[0][0],lines[0][1])]
    s_sector = [[j,j+1] for j in range(lines[1][0],lines[1][1])]
    t_sector = [[k,k+1] for k in range(lines[2][0],lines[2][1])]
    total_sector = [[x,x+1] for x in range(first_dot, last_dot)]
    count_dict = {y:0 for y in range(first_dot, last_dot)}

    for sec in total_sector:
        count_dict[sec[0]] += f_sector.count(sec)
        count_dict[sec[0]] += s_sector.count(sec)
        count_dict[sec[0]] += t_sector.count(sec)
    
    for k,v in count_dict.items():
        if v >= 2 :
            answer += 1
    
    return answer

print(solution([[0, 1], [2, 5], [3, 9]]))




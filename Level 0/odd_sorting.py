# 특이한 정렬

def solution(numlist, std):
    # 절대값 씌운 차이값 list
    difference = [num - std for num in numlist]
    distance = [num - std if num - std >= 0 else std - num for num in numlist]    
    distance.sort()
    
    # 반복되는 숫자가 나올경우 뒤에 숫자를 음수로 변환
    for idx in range(len(distance)-1):
         if distance[idx] == distance[idx+1]:
            distance[idx+1] = -distance[idx]
    
    # 절대값 씌워서 원본과 다른 경우 바꿔주는 과정
    for idx in range(len(distance)):
        if distance[idx] not in difference:
            distance[idx] = -distance[idx]
        
    answer = [d+std for d in distance]
    
    return answer

solution([1, 2, 3, 4, 5, 6],4)

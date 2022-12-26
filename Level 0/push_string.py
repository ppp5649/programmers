# 문자열 밀기

def solution(A, B):
    answer = 0
    A_list = list(A)
    B_list = list(B)
    
    for i in range(len(A)):
        A_list.insert(0,A_list.pop())
        answer += 1
        if A_list != B_list:
            if answer == len(A):
                answer = -1
                break
            else:
                continue
        
        else:
            if answer == len(A):
                answer = 0
            else:
                break
            
    return answer

# deque를 이용한 풀이 - pop이나 insert보다 연산이 빠름
from collections import deque

def solution(A,B):
    a, b = deque(A), deque(B)
    
    for cnt in range(len(A)):
        if a == b:
            return cnt
        
        a.rotate()
    
    return -1

# 문자열 자체 슬라이싱 이용

def solution(A,B):
    for cnt in range(len(A)):
        if A == B:
            return cnt
        # 문자열은 수정 불가능하기 때문에 재선언하면 됨
        A = A[-1] + A[:-1]
    
    return -1

# 신박한 풀이 - 문자열 두개를 합쳐서 find로 찾는 방법

def solution(A,B):
    BB = B*2
    return BB.find(A)

# 로그인 성공
def solution(id_pw, db):
    db_dict ={data[0]:data[1] for data in db}
    ID, PW = id_pw[0], id_pw[1]
    
    if ID in db_dict:
        answer = 'login' if db_dict[ID] == PW else 'wrong pw'
    
    else:
        answer = 'fail'

    return answer 
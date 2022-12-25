# 모스부호 (1)

def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
 
    code_list = letter.split()
    decode_list = [morse[code] for code in code_list]
    answer = "".join(decode_list)
    
    return answer
    
    

print(solution(".... . .-.. .-.. ---"))
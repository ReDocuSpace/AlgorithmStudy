def solution(strArr):
    answer = []
    for str in strArr:
        
        if str.find('ad') == -1:
            answer.append(str)
   
    return answer
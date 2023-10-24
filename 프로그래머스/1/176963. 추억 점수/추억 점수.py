def solution(name, yearning, photo):
    answer = []
    
    dic = { idx:value for idx, value in zip(name, yearning) }    

    for item in photo:
        score = 0
        for index in item:    
            if dic.get(index) != None:
                score += dic[index] 
        
        answer.append(score)
        
    return answer
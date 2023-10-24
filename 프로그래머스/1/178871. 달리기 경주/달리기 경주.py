def solution(players, callings):    
    
    
    playerDic = {player: int(idx) for idx, player in enumerate(players)}
    
    for call in callings:
        current_rank = playerDic[call]
        
        playerDic[call] -= 1
        playerDic[players[current_rank - 1]] += 1
        
        players[current_rank - 1], players[current_rank] = call, players[current_rank - 1]

    
    return players
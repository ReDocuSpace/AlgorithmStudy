def solution(park, routes):

    # 로봇 강아지
    robot_dog = [0,0]

    # 강아지 현재 위치 찾기
    for y, x in enumerate(park):
        if "S" in x:
            robot_dog[0] = y
            robot_dog[1] = x.index("S")
            break

    for y in range(len(park)):
        for x in range(len(park[y])):
            if park[y][x] == 'S':
                robot_dog[0] = y
                robot_dog[1] = x
                break
                
    for route in routes:
        
        command = route[0]
        count = int(route[2:])
        
        direct = [0,0]
        # EWSN [0,0] y,x 방향세팅

        if command == 'E':
            direct[1] = 1
        elif command == 'W':
            direct[1] = -1
        elif command == 'S':
            direct[0] = 1
        elif command == 'N':
            direct[0] = -1
        
        move = robot_dog
        
        moveCheck = True
        for i in range(count):
            check = [0,0]
            check[0] = move[0] + (direct[0] * (i + 1)) 
            check[1] = move[1] + (direct[1] * (i + 1))
            
            if check[0] < 0 or check[1] < 0 or check[0] > len(park) - 1 or check[1] > len(park[0]) - 1:
                moveCheck = False
                break
            
            if len(park) >= check[0] and len(park[0]) >= check[1]:
                if park[check[0]][check[1]] == 'X':
                    moveCheck = False
                    break
        
        if moveCheck == True:
            robot_dog[0] = move[0] + (direct[0] * (i + 1)) 
            robot_dog[1] = move[1] + (direct[1] * (i + 1))

    return robot_dog
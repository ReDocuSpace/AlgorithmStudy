def solution(a, b):
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    sum = -1
    for i in range(a - 1):
        sum += days[i]
    
    return (week[int(sum + b) % 7])
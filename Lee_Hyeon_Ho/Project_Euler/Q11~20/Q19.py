year = 1901
month = 1
day = 1
week = 0 #월요일임 7%week => 요일
cnt = 0
month30 = [4,6,9,11]

while year < 2021:
    last_day = 0
    if month == 2:
        if year%400 != 0 and year%100 == 0:  # 윤년인 경우
            last_day = 29
        else:  # 윤년이 아닌 경우
            last_day = 28
    elif month in month30:
        last_day = 30
    else:
        last_day = 31
        
    while day <= last_day:
        day += 7
    
    month += 1
    day -= last_day
    
    if month == 13:
        month -= 12
        year += 1
    
    if year == 2001:
        break
    
    if day == 1:
        cnt += 1
    
print(cnt)

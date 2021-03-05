def date_list(date:str) -> list:
    days = date.split(",")
    c_days = [] #converted date
    for day in days:
        c_days.append(int(day))
        assert int(day) > 0 and int(day) <= 7

    return c_days

def date_str(date:list or tuple) -> str:
    c_date = "" #converted date
    for day in date:
        c_date += str(day) + ","
    
    return c_date[:-1]

def hour_list(hour:str) -> list:
    c_hour = hour.split(":")
    assert len(c_hour) == 2
    
    c_hour[0] = int(c_hour[0])
    c_hour[1] = int(c_hour[1])

    assert c_hour[0] < 24 and c_hour[0] >= 0
    assert c_hour[1] < 60 and c_hour[1] >= 0

    return c_hour

a = hour_list("23:00") 
print(a)
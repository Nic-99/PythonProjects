
def add_time(start, duration, dayName = None):
    week = {"monday":1, "tuesday":2, "wednesday":3, "thursday":4, "friday":5, "saturday":6, "sunday":7}
    AMPM = start.split(" ")[1]
    duration = int(duration.split(':')[0])*60 + int(duration.split(':')[1])
    start = int(start.split(" ")[0].split(':')[0])*60 + int(start.split(" ")[0].split(':')[1])
    newTime = start + duration
    
    days = int((newTime - newTime%1440)/1440)
    hour = int( ( (newTime - days*1440) - (newTime - days*1440) %60) /60 )
    minutes = f"{(newTime%60):02}"

    if AMPM == "AM":
        if hour == 12:
            if days == 0: newTime = [str(hour), ":", minutes, " PM", ""]
            if days == 1: newTime = [str(hour), ":", minutes, " PM", "", " (next day)"]
            if days >1: newTime = [str(hour), ":", minutes, " PM", "", " ("+str(days)+ " days later)"]
        if hour < 12:
            if days == 0: newTime = [str(hour), ":", minutes, " AM", ""]
            if days == 1: newTime = [str(hour), ":", minutes, " AM", "", " (next day)"]
            if days >1: newTime = [str(hour), ":", minutes, " AM", "", " ("+str(days)+ " days later)"]
        if hour > 12:
            hour = hour - 12
            if days == 0: newTime = [str(hour), ":", minutes, " PM", ""]
            if days == 1: newTime = [str(hour), ":", minutes, " PM", "", " (next day)"]
            if days >1: newTime = [str(hour), ":", minutes, " PM", "", " ("+str(days)+ " days later)"]
    else:
        if hour == 12 and days != 0:
            days +=1
            newTime = [str(hour), ":", minutes, " AM", "", " ("+str(days)+ " days later)"]
        if hour < 12:
            newTime = [str(hour), ":", minutes, " PM", ""]
        if hour > 12:
            hour = hour - 12
            days +=1
            if days > 1:
                newTime = [str(hour), ":", minutes, " AM", "", " ("+str(days)+ " days later)"]
            else:
                newTime = [str(hour), ":", minutes, " AM", "", " (next day)"]
    if dayName != None:
        dayName = week.get(dayName.lower())
        weekDay = (dayName + days)%7
        if weekDay != 0:
            newTime[4] = ", " + list(week.keys())[list(week.values()).index(weekDay)].capitalize()
        else:
            newTime[4] = ", " + list(week.keys())[list(week.values()).index(dayName + 1)].capitalize()
    return ''.join(newTime)


# print(add_time("11:55 AM","3:12"))
# print(add_time("5:01 AM", "0:00"))
# print(add_time("11:40 AM", "0:25"))
# print(add_time("3:30 PM", "2:12", "Monday")) # -------> "5:42 PM, Monday"
# print(add_time("2:59 AM", "24:00", "saturDay")) # ----> "2:59 AM, Sunday (next day)"
# print(add_time("11:59 PM", "24:05", "Wednesday")) # --> "12:04 AM, Friday (2 days later)"
# print(add_time("8:16 PM", "466:02", "tuesday")) # ----> "6:18 AM, Monday (20 days later)"


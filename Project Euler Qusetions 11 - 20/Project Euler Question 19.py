#Project Euler Question 19

#You are given the following information, but you may prefer to do some research for yourself.

#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

before_start_dict = {}
before_start_sunday_counter = 0
date_dict = {}
sunday_counter = 0
start_year = 1901
start_month = 1
start_day = 1
end_year = 2000
end_month = 12
end_day = 31

weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekday_counter = 0

for years in range(1900,start_year):
    #print (years)
    for month in range(1,(12+1)):
        #print (month, years)
        if month == 2:
            if (years % 400 == 0):
                for day in range(1,(29+1)):
                    #print (day, month, years)
                    before_start_dict[day, month, years] = weekday[weekday_counter]
                    weekday_counter += 1
                    if weekday_counter == 7:
                        weekday_counter = 0
            elif (years % 100 == 0):
                for day in range(1,(28+1)):
                    #print (day, month, years)
                    before_start_dict[day, month, years] = weekday[weekday_counter]
                    weekday_counter += 1
                    if weekday_counter == 7:
                        weekday_counter = 0
            elif (years % 4 == 0):
                for day in range(1,(29+1)):
                    #print (day, month, years)
                    before_start_dict[day, month, years] = weekday[weekday_counter]
                    weekday_counter += 1
                    if weekday_counter == 7:
                        weekday_counter = 0
            else:
                for day in range(1,(28+1)):
                    #print (day, month, years)
                    before_start_dict[day, month, years] = weekday[weekday_counter]
                    weekday_counter += 1
                    if weekday_counter == 7:
                        weekday_counter = 0
        elif month in {4, 6, 9, 11}:
            for day in range(1,(30+1)):
                #print (day, month, years)
                before_start_dict[day, month, years] = weekday[weekday_counter]
                weekday_counter += 1
                if weekday_counter == 7:
                    weekday_counter = 0
        else:
            for day in range(1,(31+1)):
                #print (day, month, years)
                before_start_dict[day, month, years] = weekday[weekday_counter]
                weekday_counter += 1
                if weekday_counter == 7:
                    weekday_counter = 0

for date in before_start_dict:
    if date[1] == 1:
        #print (date)
        if before_start_dict[date] == "Sunday":
            #print (date, "Sunday")
            before_start_sunday_counter += 1

for years in range(start_year,(end_year+1)):
    #print (years)
    for month in range(1,(12+1)):
        #print (month, years)
        if month == 2:
            if (years % 400 == 0):
                for day in range(1,(29+1)):
                    #print (day, month, years)
                    date_dict[day, month, years] = weekday[weekday_counter]
                    weekday_counter += 1
                    if weekday_counter == 7:
                        weekday_counter = 0
            elif (years % 100 == 0):
                for day in range(1,(28+1)):
                    #print (day, month, years)
                    date_dict[day, month, years] = weekday[weekday_counter]
                    weekday_counter += 1
                    if weekday_counter == 7:
                        weekday_counter = 0
            elif (years % 4 == 0):
                for day in range(1,(29+1)):
                    #print (day, month, years)
                    date_dict[day, month, years] = weekday[weekday_counter]
                    weekday_counter += 1
                    if weekday_counter == 7:
                        weekday_counter = 0
            else:
                for day in range(1,(28+1)):
                    #print (day, month, years)
                    date_dict[day, month, years] = weekday[weekday_counter]
                    weekday_counter += 1
                    if weekday_counter == 7:
                        weekday_counter = 0
        elif month in {4, 6, 9, 11}:
            for day in range(1,(30+1)):
                #print (day, month, years)
                date_dict[day, month, years] = weekday[weekday_counter]
                weekday_counter += 1
                if weekday_counter == 7:
                    weekday_counter = 0
        else:
            for day in range(1,(31+1)):
                #print (day, month, years)
                date_dict[day, month, years] = weekday[weekday_counter]
                weekday_counter += 1
                if weekday_counter == 7:
                    weekday_counter = 0

for date in date_dict:
    if date[0] == 1:
        #print (date)
        if date_dict[date] == "Sunday":
            #print (date, "Sunday")
            sunday_counter += 1


print (sunday_counter, "is the number of Sundays")
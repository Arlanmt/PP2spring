from datetime import datetime, timedelta
def whereiam(n):
    current_time = datetime.now()
    return current_time - timedelta(n)

print(whereiam(5))




def yesterday():
    current_day = datetime.now().date() - timedelta(days=1)
    formatted_date = current_day.strftime("%a %d %B")
    return formatted_date
print(yesterday())




def drop_microseconds(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')


current_datetime = datetime.now()
datetime_without_microseconds = drop_microseconds(current_datetime)
print("microseconds:", current_datetime)
print(" without microseconds:", datetime_without_microseconds)



def date_difference_in_seconds(date1, date2):
    difference = date2 - date1
    return difference.total_seconds()


date_str1 = "2024-01-01 12:00:00"
date_str2 = "2024-01-01 12:30:00"

date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")

difference_seconds = date_difference_in_seconds(date1, date2)
print("Difference in seconds:", difference_seconds)


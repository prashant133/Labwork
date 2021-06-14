'''
10. Write a Python program to convert seconds to day, hour, minutes and seconds.
'''

time_in_sec = int(input('enter the time: '))
sec_in_day = time_in_sec / 86400
print(sec_in_day)
rem_sec = time_in_sec % 86400
print(rem_sec)

sec_in_hour = rem_sec / 3600
print(sec_in_hour)
sec_in_minutes = ((rem_sec)%3600) / 60
print(sec_in_minutes)
sec= sec_in_minutes % 60
print(sec)
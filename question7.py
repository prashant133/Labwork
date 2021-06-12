'''
7. You live 4 miles from university.
 The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
 How long will the bus journey take? Alternatively, you could run to university.
 You jog the first mile at 7mph; then run the next two at15mph; before jogging the last at 7mph again.
 Will this be quicker or slower than the bus?
'''
# By bus
distance = int(input('enter the distance: '))
speed_of_bus = int(input('enter the speed of bus '))
time_taken_bus_in_hrs = distance / speed_of_bus
time_taken_bus_in_min = time_taken_bus_in_hrs * 60
num=int(input('enter the number of stops: '))
time_taken_bus_at_stop_in_min = 2 * num
total_time_taken_by_bus = time_taken_bus_in_min + time_taken_bus_at_stop_in_min
print(f'time taken by bus in minutes to reach school {total_time_taken_by_bus}')
# By foot
speed_of_men_1mile = int(input('enter the speed of 1mile: '))
speed_of_men_2mile = int(input('enter the speed of 2mile: '))
speed_of_men_last_mile = int(input('enter the speed of 3mile: '))
total_speed = speed_of_men_1mile + speed_of_men_2mile + speed_of_men_last_mile
time_taken_men_in_hrs = distance / total_speed
total_time_taken_by_men = time_taken_men_in_hrs * 60
print(f'time taken by foot in minutes to reach school {total_time_taken_by_men}')
if total_time_taken_by_bus > total_time_taken_by_men :
    print(f" by foot is the faster ")
else:
    print(f'by bus is faster')


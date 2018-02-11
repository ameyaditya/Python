import datetime as dt
import time
arrival = '9:00,  9:40, 9:50,  11:00, 15:00, 18:00'
#arrival = input()
departure = '9:10, 12:00, 11:20, 11:30, 19:00, 20:00'
#departure = input()
times = []
arrival = arrival.split(', ')
departure = departure.split(', ')
arrival = [i.split(':') for i in arrival]
departure = [i.split(':') for i in departure]
for item,item2 in zip(arrival,departure):
    times.append([dt.time(int(item[0]),int(item[1])),'a'])
    times.append([dt.time(int(item2[0]),int(item2[1])),'d'])
answers = []
times = sorted(times,key = lambda x: x[0])
count = 0
for checker in times:
    if checker[1] == 'a':
        count = count + 1
    if checker[1] == 'd':
        count = count - 1
    answers.append(count)
print(max(answers))

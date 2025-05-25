
time_in_minutes = 0 # переменная для сохранения общего количества минут

time_values = '1h 45m,360s,25m,30m 120s,2h 60s'


for value in time_values.split(','): 
    value = value.replace(' ', '')
    if 'h' in value:
        hours = int(value.split('h')[0])
        time_in_minutes += hours * 60
        value = value.split('h')[1]
    if 'm' in value:
        minutes = int(value.split('m')[0])
        time_in_minutes += minutes
        value = value.split('m')[1]
    if 's' in value:
        seconds = int(value.split('s')[0])
        time_in_minutes += seconds // 60


print(time_in_minutes)



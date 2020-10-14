hours = 36
interval = 3

if hours%interval == 0:
    list_hours = [1 for i in range(hours+1)]
else:
    print('Invalid Number')

prime1 = 2

while(prime1 * prime1 <= hours):
    for i in range(prime1 * prime1, hours + 1, prime1):
        if list_hours[i] == 0:
            continue
        elif list_hours[i] == 1:
            list_hours[i] = 0
    prime1+=1

list_prime_hours = []

for i in range(1, hours+1):
    list_prime_hours.append(i * list_hours[i])

hour_parts = int(hours/interval)

segmented_days = []
for i in range(0, hours, hour_parts):
    segmented_days.append(list_prime_hours[i:i+hour_parts])

print(segmented_days)

grouped_hours = []
for i in range(12):
    for j in range(3):
        grouped_hours.append(segmented_days[j][i])

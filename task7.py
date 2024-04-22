from random import *
t = []
for i in range(31):
    t.append(randint(-10, 10))
print('Список температур за март:', t)
k = 0
low_t = 10
low_d = None
high_t = -10
for index, j in enumerate(t):
    if j > 0:
        k += 1
    if j < low_t:
        low_t = j
        low_d = index
    if j > high_t:
        high_t = j
t_dif = high_t - low_t
print('Разница между самой высокой и самой низкой температурой:', t_dif, '°C')
print('Кол-во дней, когда температура была выше нуля:', k, 'дней')
print('Самая низкая температура:', low_t, '°C, День:', low_d + 1, 'марта')
leaps = 0
for i in range(30):
    if t[i]*t[i+1] < 0:
        leaps += 1
print('Кол-во скачков температур:', leaps, 'скачков')

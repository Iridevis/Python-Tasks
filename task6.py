# Введите оценки через пробел, по завершении ввода нажмите Enter

grades = list(map(int, input().split()))
summ = 0
more_then_seven = 0;
for i in grades:
    summ = summ+i
    if i > 7:
        more_then_seven += 1

average = summ/len(grades)

print('Средняя оценка:', int(average))
print('Количество оценок выше 7:', more_then_seven)
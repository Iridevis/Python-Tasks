# Чтение входных данных 3 2 4 5 4 - 122
A = int(input())
B = int(input())
C = int(input())
D = int(input())
N = int(input())


full_cycles = N * 7 // (A + B)  # 5
remaining_days = N * 7 % (A + B)  # 0.6

total_hours_full_cycles = (A * C + B * D) * full_cycles

if remaining_days >= A:
    total_hours_remaining = A * C + min((remaining_days - A) * D, B * D)
else:
    total_hours_remaining = remaining_days * C

total_hours = total_hours_full_cycles + total_hours_remaining

print(total_hours)







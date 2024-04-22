# Чтение входных данных
# 5
# 1 2 3 4
# 1 2 3
# Считываем данные
S = int(input())
prices1 = list(map(int, input().split()))
prices2 = list(map(int, input().split()))

count = 0

i = 0
j = len(prices2) - 1

while i < len(prices1) and j >= 0:
    current_sum = prices1[i] + prices2[j]
    if current_sum == S:
        count += 1
        i += 1
        j -= 1
    elif current_sum < S:
        i += 1
    else:
        j -= 1

print(count)


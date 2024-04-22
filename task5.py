# 3
# 4 1 2 3 2
# 0
# 0
# Считываем количество колод и создаем список для хранения карт
# Считываем данные
N = int(input())
stacks = []
for _ in range(N):
    cards = list(map(int, input().split()))[1:]
    stacks.append(cards)

# Список для хранения действий
actions = []

# Проходим по каждой стопке карт
for i in range(N):
    # Проходим сверху вниз по текущей стопке
    for j in range(len(stacks[i]) - 1, -1, -1):
        # Если текущая карта не на своем месте
        if stacks[i][j] != i + 1:
            # Ищем стопку, куда переместить текущую карту
            for k in range(N):
                # Если нашли стопку, куда переместить, добавляем действие в список
                if stacks[k][-1] == i + 1:
                    actions.append((i + 1, k + 1))
                    stacks[k].append(stacks[i].pop())
                    break
            # Если не нашли подходящую стопку, значит решение не существует
            else:
                print(0)
                exit()

# Выводим последовательность действий
for action in actions:
    print(*action)




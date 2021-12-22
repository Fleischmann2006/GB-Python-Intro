# Ввод данных
gain = int(input('Выручка: '))
loss = int(input('Издержки: '))

if gain >= 0 and loss >= 0:
    if gain > loss:
        print('Вы работаете в плюс! Молодец!')
        income = gain - loss  # Расчёт прибыли
        print(f'Прибыль: {income} тугриков')
        print(f'Рентабельность: {(income / gain * 100):.1f}%')

        workers_count = int(input('Введите кол-во сотрудников: '))  # Запрос кол-ва сотрудников
        if workers_count > 0:
            print(f'В среднем каждый сотрудник заработал {(income / workers_count):.2f} тугриков(а)')
        else:
            print('Ай-ай-ай')  # А то ещё ноль введут
    elif loss > gain:
        print(f'Вы работаете в минус!\nВы потеряли {loss - gain} тугриков')
    else:
        print('С таким успехом можно и не работать...')
else:
    print('Так не бывает; не надо так делать!')

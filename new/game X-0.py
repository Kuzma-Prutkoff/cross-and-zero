field = [['.'] * 3 for _ in range(3)]  # ПОЛЕ ДЕЙСТВИЯ

def greet():			# ПРИВЕТСТВИЕ
    print('----------------')
    print('игра: крестик-нолик')
    print('правила: 2 игрока крестик - Х и нолик - 0 ходят по-очереди')
    print('формат хода: х пробел у, где х - номер строки, у - номер столбца')
    print('ПОГНАЛИ')
    print('----------------')

def field_show():		# Игровое поле
    print('                    | 0 | 1 | 2 |')  # нумерация строк
    print('                  ---------------')  # верхний разделитель
    for i, row in enumerate(field):  # enumerate сначала индекс [field], потом его значение
        row = ' | '.join(row)  # склеиваем ряд через |
        print(f'                  {i} | {row} |')  # печатаем ряд: сначала его индекс| потом элемент ряда | '.'|'.'|'.' |
        print('                  ---------------')  # разделитель между строками
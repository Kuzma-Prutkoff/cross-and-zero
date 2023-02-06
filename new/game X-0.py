field = [['.'] * 3 for _ in range(3)]  # пустое ПОЛЕ ДЕЙСТВИЯ 3 на 3

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

def user_input():		# Координаты введенные пользователем
    while True:
        coordinates = input('введи координаты своего хода через пробел:').split() # приходится вводить строку, если ввести буквы при наличии int, то выдаст ошибку
        if len(coordinates) != 2:
            print('Введи ДВЕ координаты. Не одну, не три, не ни одной, а ДВЕ')
            continue
        x,y = coordinates # переменным поочереди присваиваются значения списка, если поставить это присвоение выше, то возникнет ошибка
        if not(x.isdigit()) or not(y.isdigit()):
            print('Введи ЧИСЛА, а не буквы или символы')
            continue
        x,y = int(x),int(y) # делаем х,у числами, чтобы с ними можно было работать
        if not(0<=x<=2) or not(0<=y<=2):
            print('координаты не верны, диапазон координат от 0 до 2 ')
            continue
        if field[x][y] != '.':
            print('клетка занята')
            continue
        return x,y

def winner_winner_chicken_dinner():  # Восемь вариантов победы
    win_list = [((0,0),(0,1),(0,2)), ((1,0),(1,1),(1,2)), ((2,0),(2,1),(2,2)), ((0,0),(1,0),(2,0)),
                ((0,1),(1,1),(2,1)), ((0,2),(1,2),(2,2)), ((0,0),(1,1),(2,2)), ((0,2),(1,1),(2,0))]
    for cord in win_list: # для кортежа внутри списка - ((0,0),(0,1),(0,2)),
        inner_cord = []     # пустой список для внутреннего кортежа
        for elem in cord: # для внутреннего кортежа относительно внешнего (0,0)
            inner_cord.append(field[elem[0]][elem[1]])
        if inner_cord == ['X','X','X']:
            print(f'===============ТЫ ПОБЕДИЛ X-крестик!!!==========================')
            return True
        if inner_cord == ['0','0','0']:
            print(f'===============ТЫ ПОБЕДИЛ {inner_cord[0]}!!!====================')
            return True
    return False

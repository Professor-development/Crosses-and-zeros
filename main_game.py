def print_matrix(mat):
    for row in mat:
        print(*row)


def win(mat):
    for row in mat:
        if row[1] == row[2] == row[3] != '-':
            return True
    for column in range(1, 4):
        if mat[1][column] == mat[2][column] == mat[3][column] != '-':
            return True
    if mat[1][1] == mat[2][2] == mat[3][3] != '-':
        return True
    if mat[3][1] == mat[2][2] == mat[1][3] != '-':
        return True
    return False


def user_input(matrix, mot):
    player = ('крестики', 'нолики')[mot % 2]
    user_in = input(f"Ходят {player}. Введите координаты хода в формате - X Y: ")
    if check(user_in, matrix):
        user_in = list(map(int, user_in.split()))
        return user_in
    else:
        return user_input(matrix, mot)


def check(position, matrix):
    if len(position) != 3:
        print("Недопустимый формат ввода")
        return False
    elif position[1] == " " and (position[0] != " " and position[2] != " "):
        position_check = list(position.split())
    else:
        print("Недопустимый формат ввода")
        return False
    if position_check[0].isalpha() or position_check[1].isalpha():
        print("Недопустимый формат ввода")
        return False
    else:
        position_check = list(map(int, position_check))
    if position_check[1] > 3 or position_check[1] < 1 or position_check[0] > 3 or position_check[0] < 1:
        print("Координаты находяться за пределами ввода, введите корректные координаты!")
        return False
    elif matrix[position_check[1]][position_check[0]] == "-":
        return True
    else:
        print("Данная клетка уже занята, введите другие координаты!")
        return False


def game(matrix):
    print("Приветствую вас! Это игра крестники нолики, хорошей игры! ")
    print_matrix(matrix)
    for motion in range(9):
        position = user_input(matrix, motion)
        if motion % 2 == 0:
            matrix[position[1]][position[0]] = "X"
        else:
            matrix[position[1]][position[0]] = "O"
        if win(matrix):
            print("Победили крестики. Поздравляю!") if motion % 2 == 0 else print("Победили нолики. Поздравляю!")
            print_matrix(matrix)
            break
        if motion == 8:
            print("Ничья!")
            print_matrix(matrix)
            break
        print_matrix(matrix)


game_place = [[" ", 1, 2, 3], [1, '-', '-', '-'], [2, '-', '-', '-'], [3, '-', '-', '-']]

game(game_place)
print("Нажмите Enter, чтобы выйти из программы")
input()

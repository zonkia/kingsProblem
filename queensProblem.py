def print_board(board):
    for row in board:
        print(row)


def print_solutions(tuples):
    for solution in tuples:
        print_board(solution)
        print()


def get_unique_solutions(solutions):
    uniqueSolutions = []
    for solution in solutions:
        if solution not in uniqueSolutions:
            uniqueSolutions.append(solution)
    return uniqueSolutions


def get_clear_board(n):
    return [[0
             for _ in range(n)
             ]
            for _ in range(n)
            ]


def convert_to_tuple_board(board):
    tupleList = []
    for row in board:
        tupleList.append(tuple(row))
    return tuple(tupleList)


def get_column(board, x):
    column = []
    for row in board:
        column.append(row[x])
    return column


def get_first_diagonal(board, y, x, n):
    diagonal = []
    for step in range(1, n+1):
        if (y-step) < 0 or (x-step) < 0:
            continue
        else:
            diagonal.append(board[y-step][x-step])
    for step in range(1, n+1):
        if (y+step) > n-1 or (x+step) > n-1:
            continue
        else:
            diagonal.append(board[y+step][x+step])
    return diagonal


def get_second_diagonal(board, y, x, n):
    diagonal = []
    for step in range(1, n+1):
        if (y-step) < 0 or (x+step) > n-1:
            continue
        else:
            diagonal.append(board[y-step][x+step])
    for step in range(1, n+1):
        if (y+step) > n-1 or (x-step) < 0:
            continue
        else:
            diagonal.append(board[y+step][x-step])
    return diagonal


def check_position(board, y, x, n):
    if board[y][x] != 0:
        return False
    if 1 in board[y]:
        return False
    if 1 in get_column(board, x):
        return False
    if 1 in get_first_diagonal(board, y, x, n):
        return False
    if 1 in get_second_diagonal(board, y, x, n):
        return False
    return True


def check_if_solved(board, n):
    amountOfKings = 0
    for row in board:
        for position in row:
            if position == 1:
                amountOfKings += 1
    if amountOfKings == n:
        return True
    else:
        return False


def solve(board, y, x, n, boardSize, y0, x0, solutions):
    if check_if_solved(board, n):
        solutions.append(convert_to_tuple_board(board))
        # print_board(board)
        return True

    for row in range(boardSize):
        for column in range(boardSize):
            if row < y0 and column < x0:
                continue
            if board[y][x] == 0:
                if check_position(board, y, x, boardSize):
                    board[y][x] = 1
                    solve(board, row, column, n, boardSize, y0, x0, solutions)
                    board[y][x] = 0


def find_solution(solutions, boardSize, numberOfKings):
    board = get_clear_board(boardSize)
    n = numberOfKings
    for row in range(boardSize):
        for column in range(boardSize):
            if solve(board, row, column, n, boardSize, row, column, solutions):
                board = get_clear_board(boardSize)
                continue


if __name__ == "__main__":
    solutions = []
    find_solution(solutions, boardSize=5, numberOfKings=5)
    print_solutions(get_unique_solutions(solutions))
    print("Number of solutions:", len(get_unique_solutions(solutions)))

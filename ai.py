import random
import tic_tac_toe
from typing import List
from ai_difficulty_enum import AiDifficulty


def get_ai_move(difficulty: AiDifficulty, board: List[List[str]]) -> List[int]:
    if difficulty == AiDifficulty.easy:
        coordinates: List[int] = [0, 0]
        while True:
            coordinates[0] = random.randint(0, 2)
            coordinates[1] = random.randint(0, 2)
            if tic_tac_toe.board_full(board):
                tic_tac_toe.tie_screen(board)
                exit(0)
            if not ai_is_occupied(coordinates, board):
                return coordinates
    else:
        if difficulty == AiDifficulty.unbeatable:
            if not ai_is_occupied([1, 1], board):
                return [1, 1]
        coordinates: List[int] = check_for_easy_win(board)
        if not coordinates == [5, 5]:
            return coordinates
        while True:
            coordinates[0] = random.randint(0, 2)
            coordinates[1] = random.randint(0, 2)
            if tic_tac_toe.board_full(board):
                tic_tac_toe.tie_screen(board)
                exit(0)
            if not ai_is_occupied(coordinates, board):
                return coordinates


def ai_is_occupied(optimized_coordinates: List[int], board: List[List[str]]) -> bool:
    return False if board[optimized_coordinates[0]][optimized_coordinates[1]] == "." else True


def check_for_easy_win(board: List[List[str]]) -> List[int]:
    x_counter: int = 0
    o_counter: int = 0
    easy_win_position: List[int] = []
    empty_space_found: bool = False
    # check rows
    for i in range(len(board)):
        empty_space_found = False
        for j in range(len(board[0])):
            if board[i][j] == "X":
                x_counter += 1
            elif board[i][j] == "O":
                o_counter += 1
            elif board[i][j] == ".":
                easy_win_position = [i, j]
                empty_space_found = True
        if (x_counter == 2 or o_counter == 2) and empty_space_found:
            return easy_win_position
        x_counter = 0
        o_counter = 0
    # check columns
    for i in range(len(board)):
        empty_space_found = False
        for j in range(len(board[0])):
            if board[j][i] == "X":
                x_counter += 1
            elif board[j][i] == "O":
                o_counter += 1
            elif board[j][i] == ".":
                easy_win_position = [j, i]
                empty_space_found = True
        if (x_counter == 2 or o_counter == 2) and empty_space_found:
            return easy_win_position
        x_counter = 0
        o_counter = 0
    # check diagonals
    empty_space_found = False
    for i in range(len(board)):
        if board[i][i] == "X":
            x_counter += 1
        elif board[i][i] == "O":
            o_counter += 1
        elif board[i][i] == ".":
            easy_win_position = [i, i]
            empty_space_found = True
    if (x_counter == 2 or o_counter == 2) and empty_space_found:
        return easy_win_position
    x_counter = 0
    o_counter = 0
    empty_space_found = False
    for i in range(len(board)):
        if board[i][2 - i] == "X":
            x_counter += 1
        elif board[i][2 - i] == "O":
            o_counter += 1
        elif board[i][2 - i] == ".":
            easy_win_position = [i, 2 - i]
            empty_space_found = True
    if (x_counter == 2 or o_counter == 2) and empty_space_found:
        return easy_win_position
    return [5, 5]  # return this out of range value if no easy win position was found

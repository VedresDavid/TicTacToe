import time
from typing import List

from readchar import readkey

import ai
import audio
import ui
import utility
from ai_difficulty_enum import AiDifficulty
from color_enum import Color
from game_mode_select_enum import GameMode
from utility import clear_screen


def init_board(row: int = 3, column: int = 3) -> List[List[str]]:
    return [["." for i in range(column)] for i in range(row)]


def print_board(board) -> None:
    print("   1   2   3")
    colored_text = ""
    for i in range(len(board)):
        print(f"{chr(i + 65)}  ", end="")
        for j in range(len(board[0])):
            if board[i][j] == "X":
                colored_text = utility.color_text(board[i][j], Color.red)
            elif board[i][j] == "O":
                colored_text = utility.color_text(board[i][j], Color.blue)
            else:
                colored_text = board[i][j]
            print(colored_text, end="")
            print(" | ", end="")
        print()


def win_screen(x_turn: bool, board: List[List[str]]) -> None:
    utility.clear_screen()
    print_board(board)
    print(f"{'X' if x_turn else 'O'} won.")


def tie_screen(board: List[List[str]]) -> None:
    utility.clear_screen()
    print_board(board)
    print("this is a tie")


def goodbye_screen() -> None:
    print("Goodbye!")
    exit(0)


def play() -> None:
    is_gameover: bool = False
    x_turn: bool = True
    board = init_board()
    ui.main_menu("./music/Shape of You.ogg", True)
    game_mode: GameMode = ui.game_mode_selection_menu()
    if game_mode == GameMode.ai_vs_ai:
        ai_difficulty: AiDifficulty = AiDifficulty.medium
        while not is_gameover:
            utility.clear_screen()
            print_board(board)
            time.sleep(1)
            coordinates: List[int] = ai.get_ai_move(ai_difficulty, board)
            board = place(x_turn, coordinates, board)
            if anyone_won(x_turn, board):
                win_screen(x_turn, board)
                break
            elif board_full(board):
                tie_screen(board)
                break
            else:
                x_turn = change_player(x_turn)
    if game_mode == GameMode.player_vs_ai:
        ai_difficulty: AiDifficulty = ui.ai_difficulty_menu()
        if ai_difficulty == AiDifficulty.unbeatable:
            x_turn = False
        while not is_gameover:
            utility.clear_screen()
            print_board(board)
            print(f"{'X' if x_turn else 'O'} turn.")
            if x_turn:
                coordinates: List[int] = get_move(board)
                board = place(x_turn, coordinates, board)
            else:
                coordinates: List[int] = ai.get_ai_move(ai_difficulty, board)
                time.sleep(1)
                board = place(x_turn, coordinates, board)
            if anyone_won(x_turn, board):
                win_screen(x_turn, board)
                break
            elif board_full(board):
                tie_screen(board)
                break
            else:
                x_turn = change_player(x_turn)
    if game_mode == game_mode.player_vs_player:
        while not is_gameover:
            utility.clear_screen()
            print_board(board)
            print(f"{'X' if x_turn else 'O'} turn.")
            coordinates: List[int] = get_move(board)
            board = place(x_turn, coordinates, board)
            if anyone_won(x_turn, board):
                win_screen(x_turn, board)
                break
            elif board_full(board):
                tie_screen(board)
                break
            else:
                x_turn = change_player(x_turn)


def optimize_coordinates(unoptimized_coordinates: List) -> List[int]:
    return [ord(unoptimized_coordinates[0]) - 97, unoptimized_coordinates[1] - 1]


def valid_coordinates(unoptimized_coordinates: List) -> bool:
    if unoptimized_coordinates[0].lower() in ("a", "b", "c") and unoptimized_coordinates[1] in (1, 2, 3):
        return True
    audio.play_sound("./sounds/occupied.wav")
    return False


def occupied(optimized_coordinates: List[int], board: List[List[str]]) -> bool:
    if board[optimized_coordinates[0]][optimized_coordinates[1]] == ".":
        return False
    audio.play_sound("./sounds/occupied.wav")
    return True


def get_move(board: List[List[str]]) -> List[int]:
    unoptimized_coordinates = ["f", 9]  # the values have no meaning. they are only for list size.
    while True:
        clear_screen()
        print_board(board)
        print("Choose a letter (A, B, C):")
        unoptimized_coordinates[0] = readkey()
        if unoptimized_coordinates[0] == "q":
            goodbye_screen()
        print("Choose a number (1, 2, 3):")
        second_coordinate: str = readkey()
        if str(second_coordinate) == "q":
            goodbye_screen()
        try:
            unoptimized_coordinates[1] = int(second_coordinate)
        except ValueError:
            pass
        if valid_coordinates(unoptimized_coordinates) and not occupied(optimize_coordinates(unoptimized_coordinates), board):
            return optimize_coordinates(unoptimized_coordinates)


def place(x_turn: bool, coordinates: List[int], board: List[List[str]]) -> List[List[str]]:
    element_to_draw: str = "X" if x_turn else "O"
    if x_turn:
        audio.play_sound("./sounds/x_place.wav")
    else:
        audio.play_sound("./sounds/o_place.wav")
    board[coordinates[0]][coordinates[1]] = element_to_draw
    return board


def anyone_won(x_turn: bool, board: List[List[str]]) -> bool:
    element: str = "X" if x_turn else "O"
    for j in range(len(board[0])):
        if board[j][0] == element and board[j][1] == element and board[j][2] == element:
            return True
    for i in range(len(board[0])):
        if board[0][i] == element and board[1][i] == element and board[2][i] == element:
            return True
    if board[0][0] == element and board[1][1] == element and board[2][2] == element:
        return True
    if board[0][2] == element and board[1][1] == element and board[2][0] == element:
        return True
    return False


def board_full(board: List[List[str]]) -> bool:
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ".":
                return False
    return True


def change_player(x_turn: bool) -> bool:
    return not x_turn


if __name__ == "__main__":
    audio.pygame.init()
    audio.play_background_music("./music/Shape of You.ogg")
    play()

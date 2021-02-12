from color_enum import Color
from typing import List
import readchar
from ai_difficulty_enum import AiDifficulty
from game_mode_select_enum import GameMode
import audio
import utility


def main_menu(selected_song: str, is_music_on: bool) -> None:
    utility.clear_screen()
    print("""
1, Play
2, Options
3, Exit""")
    character: int = 0
    while character not in (1, 2, 3):
        try:
            character = int(readchar.readkey())
        except ValueError:
            pass
    utility.clear_screen()
    if character == 1:
        return
    elif character == 2:
        options_menu(selected_song, is_music_on)
    elif character == 3:
        exit(0)


def ai_difficulty_menu() -> AiDifficulty:
    utility.clear_screen()
    print("""
1, Easy
2, Medium
3, Unbeatable""")
    character: int = 0
    while character not in (1, 2, 3):
        try:
            character = int(readchar.readkey())
        except ValueError:
            pass
        utility.clear_screen()
    return {1: AiDifficulty.easy,
            2: AiDifficulty.medium,
            3: AiDifficulty.unbeatable}.get(character) or AiDifficulty.easy


def game_mode_selection_menu() -> GameMode:
    utility.clear_screen()
    print("""
1, Player vs Player
2, Player vs Ai
3, Ai vs Ai""")
    character: int = 0
    while character not in (1, 2, 3):
        try:
            character = int(readchar.readkey())
        except ValueError:
            pass
        utility.clear_screen()
    return {1: GameMode.player_vs_player,
            2: GameMode.player_vs_ai,
            3: GameMode.ai_vs_ai}.get(character) or GameMode.player_vs_player


def options_menu(selected_song: str, is_music_on: bool) -> None:
    song_names: List[str] = ["8 bit", "Chill", "Shape of You"]
    music_on_off_text: List[str] = ["Music Off", "Music On"]
    song1 = "./music/8 bit.ogg"
    song2 = "./music/chill.ogg"
    song3 = "./music/Shape of You.ogg"
    if is_music_on:
        music_on_off_text[1] = utility.color_text(music_on_off_text[1], Color.blue)
    else:
        music_on_off_text[0] = utility.color_text(music_on_off_text[0], Color.red)
    if selected_song == song1:
        song_names[0] = utility.color_text(song_names[0], Color.blue)
    elif selected_song == song2:
        song_names[1] = utility.color_text(song_names[1], Color.blue)
    elif selected_song == song3:
        song_names[2] = utility.color_text(song_names[2], Color.blue)
    utility.clear_screen()
    print(f"""
----- Controls -----
1, {music_on_off_text[0]}
2, {music_on_off_text[1]}
----- Song Selection -----
3, {song_names[0]}
4, {song_names[1]}
5, {song_names[2]}
--------------------------
6, Back""")
    character: int = 0
    while character not in (1, 2, 3, 4, 5, 6):
        try:
            character = int(readchar.readkey())
        except ValueError:
            pass
        utility.clear_screen()
        if character == 1:
            audio.switch_music_off()
            is_music_on = False
            options_menu(selected_song, is_music_on)
        elif character == 2:
            audio.switch_music_on(selected_song)
            is_music_on = True
            options_menu(selected_song, is_music_on)
        elif character == 3:
            audio.play_background_music(song1)
            selected_song = song1
            options_menu(selected_song, True)
        elif character == 4:
            audio.play_background_music(song2)
            selected_song = song2
            options_menu(selected_song, True)
        elif character == 5:
            audio.play_background_music(song3)
            selected_song = song3
            options_menu(selected_song, True)
        elif character == 6:
            main_menu(selected_song, is_music_on)

import os
from color_enum import Color


def color_text(text: str, color: Color) -> str:
    return {Color.red: "\033[91m" + text + "\033[00m",
            Color.blue: "\033[96m" + text + "\033[00m",
            Color.yellow: "\033[93m" + text + "\033[00m",
            Color.green: "\033[92m" + text + "\033[00m",
            Color.purple: "\033[95m" + text + "\033[00m",
            Color.black: text}.get(color) or text


def clear_screen() -> None:
    os.system("cls") if os.name == "nt" else os.system("clear")

import pygame


def play_sound(path: str) -> None:
    sound = pygame.mixer.Sound(path)
    sound.play()


def play_background_music(path: str) -> None:
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)


def switch_music_on(path: str) -> None:
    play_background_music(path)


def switch_music_off() -> None:
    pygame.mixer.music.stop()

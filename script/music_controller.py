__author__ = 'Pawel'

import os
from pygame import mixer

local_dir = os.path.dirname(__file__)
music_path = os.path.join(local_dir, "sounds", "menu_sound.mp3")


class MusicController(object):
    def __init__(self):
        self.set_music()

    @staticmethod
    def set_music():
        mixer.music.load(music_path)

    @staticmethod
    def play_music():
        mixer.music.play(0)

    @staticmethod
    def stop_music():
        mixer.music.stop()

    @staticmethod
    def pause_music():
        mixer.music.pause()

    @staticmethod
    def un_pause_music():
        mixer.music.unpause()

    @staticmethod
    def set_volume(value):
        mixer.music.set_volume(value)
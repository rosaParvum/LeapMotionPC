import ctypes
from keyboard import press_and_release
from time import sleep
import win32api
from os import system

def pausePlay():
    VK_MEDIA_PLAY_PAUSE = 0xB3
    hwcode = win32api.MapVirtualKey(VK_MEDIA_PLAY_PAUSE, 0)
    win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, hwcode)

def lock():
    ctypes.windll.user32.LockWorkStation()

def adminConsole():
    system("cscript adminShell.vbs")

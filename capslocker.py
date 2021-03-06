# pip install pynput
# pip install pystray

import ctypes

from pynput import keyboard
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw


CAPSLOCK = 0x14


class CapsLocker(object):

    def __init__(self):
        systraymenu = Menu(MenuItem("Toggle", self.togglelock), MenuItem("Quit", self.quit))

        self.user32 = ctypes.WinDLL('user32')
        self.user32.GetKeyState.restype = ctypes.c_short

        self.lock = True;
        self.lockedicon = Image.open("CapsLockerOn.png")
        self.unlockedicon = Image.open("CapsLockerOff.png")
        
        self.keyboard = keyboard.Controller()
        self.listener = keyboard.Listener(on_release = self.watchcapslock)
        self.listener.start()

        self.systray = Icon('CapsLocker', menu = systraymenu)
        self.systray.icon = self.lockedicon
        self.systray.run()


    def watchcapslock(self, key):
        if self.lock and self.getcapslock() and key == keyboard.Key.caps_lock:
            self.switchcapslock()

    def switchcapslock(self):
        self.keyboard.press(keyboard.Key.caps_lock)
        self.keyboard.release(keyboard.Key.caps_lock)

    def getcapslock(self):
        keystate = self.user32.GetKeyState(CAPSLOCK)
        return (keystate & 0xffff) != 0

    def togglelock(self):
        if self.lock:
            self.lock = False        
            self.systray.icon = self.unlockedicon
        else:
            self.lock = True
            self.systray.icon = self.lockedicon
            if self.getcapslock():
                self.switchcapslock()

    def quit(self):
        self.systray.stop()

CapsLocker()


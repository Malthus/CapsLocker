# pip install pynput
# pip install pystray

from pynput import keyboard
from keylock import KeyLockState
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw


class CapsLocker(object):

    def __init__(self):
        systraymenu = Menu(MenuItem("Toggle", self.togglelock), MenuItem("Quit", self.quit))

        self.lock = True;
        self.lockedicon = Image.open("CapsLockerOn.png")
        self.unlockedicon = Image.open("CapsLockerOff.png")
        self.keylockstate = KeyLockState()
        
        self.keyboard = keyboard.Controller()
        self.listener = keyboard.Listener(on_release = self.watchcapslock)
        self.listener.start()

        self.systray = Icon('CapsLocker', menu = systraymenu)
        self.systray.icon = self.lockedicon
        self.systray.run()


    def watchcapslock(self, key):
        if self.lock and self.keylockstate.getcapslock() and key == keyboard.Key.caps_lock:
            self.switchcapslock()

    def switchcapslock(self):
        self.keyboard.press(keyboard.Key.caps_lock)
        self.keyboard.release(keyboard.Key.caps_lock)

    def togglelock(self):
        if self.lock:
            self.lock = False        
            self.systray.icon = self.unlockedicon
        else:
            self.lock = True
            self.systray.icon = self.lockedicon
            if self.keylockstate.getcapslock():
                self.switchcapslock()

    def quit(self):
        self.systray.stop()

CapsLocker()


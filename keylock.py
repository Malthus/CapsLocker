# KeyLock Library

# pip install pywin32

import ctypes
import win32com.client as win32comclient


CAPSLOCK = 0x14
NUMLOCK = 0x90 
SCROLLLOCK = 0x91


class KeyLockState(object):
    def __init__(self):
        self.user32 = ctypes.WinDLL('user32')
        self.user32.GetKeyState.restype = ctypes.c_short
        self.wshell = win32comclient.Dispatch("WScript.Shell")

    def getcapslock(self):
        keystate = self.user32.GetKeyState(CAPSLOCK)
        return (keystate & 0xffff) != 0

    def togglecapslock(self):
        self.wshell.SendKeys("{CAPSLOCK}")

    def setcapslock(self):
        if not self.getcapslock():
            self.togglecapslock()

    def clearcapslock(self):
        if self.getcapslock():
            self.togglecapslock()


# CapsLocker

CapsLocker is a small Python script that switches off the CapsLock key. Each time you (accidentally) press the CapsLock key, CapsLocker will immediately turn it off again. 
CapsLocker is made for Windows. A small icon in the system tray can be used to toggle CapsLocker on and off, and to quit CapsLocker.

Use this program at your own risk!


## Installation

CapsLocker requires Python 3 to run on your computer. It uses two Python libraries that are probably not included in your Python distribution. You can manually install those libraries with:

- pip install pynput
- pip install pystray

You can run CapsLocker on the command-line with "pythonw.exe capslocker.py", or add a similar command to a Windows shortcut (assuming that Python is included in your path).


## Use

When you run CapsLocker, a small icon appears in the system tray (probably in the lower right corner of the screen), and the CapsLock key is turned off. 

![Green icon](https://raw.githubusercontent.com/Malthus/CapsLocker/master/CapsLockerOn.png) The green icon shows that CapsLocker is active, switching off your CapsLock if necessary.  
![Red icon](https://raw.githubusercontent.com/Malthus/CapsLocker/master/CapsLockerOff.png) The red icon shows that Capslocker is disabled and you can use the CapsLock key normally.

If you right-click on the CapsLocker icon in the system tray, a menu with two options appears:
 
- The **Toggle** option switches CapsLocker on or off. If the CapsLocker icon in the system tray is green, CapsLocker is active. If the icon is red, CapsLocker is disabled.
- The **Quit** option stops CapsLocker. The icon should disappear from the system tray.

It is possible to run multiple instances of CapsLocker at the same time. This is not very useful. If you rum multiple instances and you want to use CapsLock, you'll have to turn off all instances individually.


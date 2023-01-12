import win32con
import win32gui
from pyautogui import size

class Window:
    def __init__(self, title):
        self.title = title
        self.handle = win32gui.FindWindow(None, title)
        
    def getRect(self):
        left, top, right, bottom = win32gui.GetWindowRect(self.handle)
        return { 'x': left, 'y': top, 'width': right - left, 'height': bottom - top }
    
    def isExist(self):
        return self.handle != 0
    
    # 是否最小化
    def isIconic(self):
        return win32gui.IsIconic(self.handle)
    
    # 是否在前台
    def isInForeground(self):
        return self.handle == win32gui.GetForegroundWindow()
        
    def show(self):
        if self.isIconic():
            win32gui.ShowWindow(self.handle, win32con.SW_RESTORE)
        if not self.isInForeground():
            win32gui.SetForegroundWindow(self.handle)
    
    # 使窗体居中
    def center(self):
        if self.isInForeground():
            rect = self.getRect()
            screenWidth, screenHeight = size()
            win32gui.SetWindowPos(
                self.handle,
                win32con.HWND_TOP,
                screenWidth // 2 - rect['width'] // 2,
                screenHeight // 2 - rect['height'] // 2,
                rect['width'],
                rect['height'],
                win32con.SWP_NOACTIVATE | win32con.SWP_NOSIZE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW
            )
        
    def hide(self):
        if self.isInForeground():
            win32gui.SetBkMode(self.handle)

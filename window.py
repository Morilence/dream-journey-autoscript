import win32con
import win32gui
from pyautogui import size as getScreenSize

class Window:
    def __init__(self, title: str):
        self.title = title
        self.handle = win32gui.FindWindow(None, title)
        
    def __getRect(self):
        left, top, right, bottom = win32gui.GetWindowRect(self.handle)
        return { 'x': left, 'y': top, 'width': right - left, 'height': bottom - top }

    def __setPos(self, x: int, y: int):
        rect = self.__getRect()
        win32gui.SetWindowPos(
            self.handle,
            win32con.HWND_TOP,
            x,
            y,
            rect['width'],
            rect['height'],
            win32con.SWP_NOACTIVATE | win32con.SWP_NOSIZE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW
        )
    
    # 窗体是否存在
    def isExist(self):
        return self.handle != 0
    
    # 是否最小化
    def isIconic(self):
        return win32gui.IsIconic(self.handle)
    
    # 是否在前台
    def isInForeground(self):
        return self.handle == win32gui.GetForegroundWindow()
    
    # 展示
    def show(self):
        if self.isIconic():
            win32gui.ShowWindow(self.handle, win32con.SW_RESTORE)
        if not self.isInForeground():
            win32gui.SetForegroundWindow(self.handle)

    # 隐藏至后台
    def hide(self):
        if self.isInForeground():
            win32gui.SetBkMode(self.handle)

    def getRect(self):
        return self.__getRect()

    # 设置窗体的坐标位置
    def setPos(self, x, y):
        if self.isInForeground():
            self.__setPos(x, y)

    # 窗体在屏幕中的对齐策略
    def setAlign(self, align: str):
        if self.isInForeground():
            rect = self.__getRect()
            screenWidth, screenHeight = getScreenSize()
            aligns = list(map(lambda s:s.strip(), align.split(',', 1)))
            aligns.sort()
            alignDict = {
                'bottom': (rect['x'], screenHeight - rect['height']),
                'bottom,left': (0, screenHeight - rect['height']),
                'bottom,right': (screenWidth - rect['width'], screenHeight - rect['height']),
                'center': (screenWidth // 2 - rect['width'] // 2, screenHeight // 2 - rect['height'] // 2),
                'center,bottom': (screenWidth // 2 - rect['width'] // 2, screenHeight - rect['height']),
                'center,left': (0, screenHeight // 2 - rect['height'] // 2),
                'center,right': (screenWidth - rect['width'], screenHeight // 2 - rect['height'] // 2),
                'center,top': (screenWidth // 2 - rect['width'] // 2, 0),
                'left': (0, rect['y']),
                'left,top': (0, 0),
                'right': (screenWidth - rect['width'], rect['y']),
                'right,top': (screenWidth - rect['width'], 0),
                'top': (rect['x'], 0)
            }
            print(','.join(aligns))
            alignX, alignY = alignDict.get(','.join(aligns), (rect['x'], rect['y']))
            self.__setPos(alignX, alignY)

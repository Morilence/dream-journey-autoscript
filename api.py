from window import Window
from pyautogui import locateOnScreen, locateCenterOnScreen, moveTo, click, doubleClick, ImageNotFoundException

class Game(Window):
    def __init__(self, title, duration = 0.2, confidence = 0.9):
        super().__init__(title)
        self.duration = duration
        self.confidence = confidence
        
    def detect(self, imgPath):
        rect = self.getRect()
        try:
            return locateOnScreen(
                imgPath,
                region=(rect['x'], rect['y'], rect['width'], rect['height']),
                confidence=self.confidence
            ) != None
        except ImageNotFoundException:
            return False
        
    def moveTo(self, imgPath):
        rect = self.getRect()
        screenX, screenY = locateCenterOnScreen(
            imgPath,
            region=(rect['x'], rect['y'], rect['width'], rect['height']),
            confidence=self.confidence
        )
        moveTo(screenX, screenY, duration=self.duration)
        return screenX, screenY
        
    def moveToAndClick(self, imgPath):
        screenX, screenY = self.moveTo(imgPath)
        click(screenX, screenY)
    
    def moveToAndDoubleClick(self, imgPath):
        screenX, screenY = self.moveTo(imgPath)
        doubleClick(screenX, screenY)
        
from window import Window
from pyautogui import locateOnScreen, locateCenterOnScreen, moveTo, click, doubleClick, ImageNotFoundException

class Game:
    def __init__(self, title: str, duration=0.2, confidence=0.9, grayscale=False):
        self.window = Window(title)
        self.duration = duration
        self.confidence = confidence
        self.grayscale = grayscale
        
    def detect(self, imgPath):
        rect = self.window.getRect()
        try:
            return locateOnScreen(
                imgPath,
                region=(rect['x'], rect['y'], rect['width'], rect['height']),
                confidence=self.confidence,
                grayscale=self.grayscale
            ) != None
        except ImageNotFoundException:
            return False
        
    def moveTo(self, imgPath):
        rect = self.window.getRect()
        screenX, screenY = locateCenterOnScreen(
            imgPath,
            region=(rect['x'], rect['y'], rect['width'], rect['height']),
            confidence=self.confidence,
            grayscale=self.grayscale
        )
        moveTo(screenX, screenY, duration=self.duration)
        return screenX, screenY
        
    def moveToAndClick(self, imgPath):
        screenX, screenY = self.moveTo(imgPath)
        click(screenX, screenY)
    
    def moveToAndDoubleClick(self, imgPath):
        screenX, screenY = self.moveTo(imgPath)
        doubleClick(screenX, screenY)
        
import time
import threading
from pynput.keyboard import Key, Listener
from resource import IMG
from api import Game

def onPress(key):
    if key == Key.esc:
        return False

def main():
    with Listener(on_press=onPress) as listener:
        gm = Game('造梦西游online,4399造梦西游online专题,造梦西游online系列')

        if not gm.isExist():
            print('[ 未找到游戏窗口 ]')
            return False

        gm.show()
        time.sleep(1)
        gm.center()
        time.sleep(1)
        while listener.running and gm.isInForeground():
            time.sleep(1)
            print('# 检测中...')
            
            if gm.detect(IMG['INTERFACE_VERS']):
                print('! 检测到游戏版本选择界面')
                gm.moveToAndClick(IMG['COMP_V3_BTN'])
                print('> 选择大闹天庭篇')
            elif gm.detect(IMG['INTERFACE_HOME']):
                print('! 检测到游戏主页')
                gm.moveToAndClick(IMG['COMP_ARCS_BTN'])
                print('> 打开存档列表')
            elif gm.detect(IMG['INTERFACE_ARCS']):
                print('! 检测到存档列表')
                if gm.detect(IMG['COMP_ARC_ITEM']):
                    print('! 检测到目标存档')
                    gm.moveToAndClick(IMG['COMP_ARC_ITEM'])
                    print('> 选择目标存档')
        
        if not gm.isInForeground():
            print('[ 游戏窗口被切至后台，脚本被迫结束 ]')
        elif not listener.running:
            print('[ 脚本结束 ]')        

if __name__ == '__main__':
    main()

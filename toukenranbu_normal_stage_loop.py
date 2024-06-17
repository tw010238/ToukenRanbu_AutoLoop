import pyautogui
import time

# time.sleep(2)
# mouse_pos = pyautogui.position()
# print(mouse_pos)


# 目錄 > 出陣 > 第五章 > 決定 > 第四節 > 部隊選擇 > 部隊三(太刀) >　出陣
def start_the_battle(Chapter,field,team):
    pyautogui.moveTo(1600,250,duration=0.2)    # 目錄
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(460,440,duration=0.2)    # 出陣
    pyautogui.click()

    # 選擇章節
    while True:
        try:
            pyautogui.locateOnScreen(r'button\return.png')
            break
        except:
            continue
    pyautogui.moveTo(x=264, y=462, duration=0.2)  # 合戰場
    pyautogui.click()
    time.sleep(0.5)
    if Chapter == '一':
        pyautogui.moveTo(x=517, y=645, duration=0.2)
    elif Chapter == '二':
        pyautogui.moveTo(x=598, y=790, duration=0.2)
    elif Chapter == '三':
        pyautogui.moveTo(x=709, y=645, duration=0.2)
    elif Chapter == '四':
        pyautogui.moveTo(x=829, y=790, duration=0.2)
    elif Chapter == '五':
        pyautogui.moveTo(x=945, y=645, duration=0.2)
    elif Chapter == '六':
        pyautogui.moveTo(x=1059, y=790, duration=0.2)
    elif Chapter == '七':
        pyautogui.moveTo(x=1187, y=645, duration=0.2)
    elif Chapter == '八':
        pyautogui.moveTo(x=1297, y=790, duration=0.2)
    pyautogui.click()
    pyautogui.moveTo(1570,935,duration=0.2)    # 決定
    pyautogui.click()
    time.sleep(0.5)

    # 選擇地區
    if field == '一':
        pyautogui.moveTo(x=484, y=640, duration=0.2)
    elif field == '二':
        pyautogui.moveTo(x=815, y=640, duration=0.2)
    elif field == '三':
        pyautogui.moveTo(x=1142, y=640, duration=0.2)
    elif field == '四':
        pyautogui.moveTo(x=1482, y=640, duration=0.2)
    pyautogui.click()
    pyautogui.moveTo(x=1575, y=936, duration=0.2)        # 部隊選擇
    pyautogui.click()
    time.sleep(0.1)

    # 部隊選擇
    if team == '一':
        pyautogui.moveTo(x=406, y=335, duration=0.2)
    elif team == '二':
        pyautogui.moveTo(x=538, y=335, duration=0.2)
    elif team == '三':
        pyautogui.moveTo(x=670, y=335, duration=0.2)
    elif team == '四':
        pyautogui.moveTo(x=802, y=335, duration=0.2)
    elif team == '五':
        pyautogui.moveTo(x=934, y=335, duration=0.2)
    pyautogui.click()
    pyautogui.moveTo(1570,920,duration=0.2)    # 出陣
    pyautogui.click()


# 下一關
def next_stage():
    while True:
        try:
            pyautogui.locateOnScreen(r'button\warnning1.PNG',confidence=0.8, grayscale = True)        # 出現重傷警告時退出。不知道為甚麼，這張圖在螢幕上找不太到，所以要調低信心度
            break
        except:
            try:
                next_button = pyautogui.locateOnScreen(r'button\next_stage.PNG')
                next_button_center = pyautogui.center(next_button)
                pyautogui.moveTo(next_button_center,duration=0.2)
                pyautogui.click()
            except:
                try:
                    pyautogui.locateOnScreen(r'button\home.PNG')
                    break
                except:
                    try:
                        formation = pyautogui.locateOnScreen(r'button\formation.PNG')
                        formation_center = pyautogui.center(formation)
                        pyautogui.moveTo(formation_center, duration=0.2)
                        pyautogui.click()
                    except:
                        try:
                            pyautogui.locateOnScreen(r'button\DMM GAMES.PNG')
                            pyautogui.moveTo(266, 994, 0.2)
                            pyautogui.click()
                            time.sleep(0.8)
                        except:
                            break

def loop(Chapter,field,team):
    start_the_battle(Chapter,field,team)
    next_stage()

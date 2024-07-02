import pyautogui
import time

# time.sleep(2)
# mouse_pos = pyautogui.position()
# print(mouse_pos)


# 目錄 > 出陣 > 第五章 > 決定 > 第四節 > 部隊選擇 > 部隊三(太刀) >　出陣
def start_the_battle(Chapter,field,team):
    index = pyautogui.locateOnScreen(r'button\001.PNG', confidence=0.8, grayscale=True)
    index_coordinate = pyautogui.center(index)
    pyautogui.moveTo(index_coordinate,duration=0.2)    # 點擊目錄
    index_start = pyautogui.locateOnScreen(r'button\index_start.PNG', confidence=0.8, grayscale=True)
    index_start_coordinate = pyautogui.center(index_start)
    pyautogui.moveTo(index_start_coordinate, duration=0.2)    # 點擊目錄的出陣
    pyautogui.click()

    # 選擇章節
    while True:    # 等畫面出來再繼續，以return鍵為準
        time.sleep(1)
        try:
            pyautogui.locateOnScreen(r'button\return.png', confidence=0.8, grayscale=True)
            break
        except:
            continue
    normal_stage = pyautogui.locateOnScreen(r'button\normal_stage.PNG', confidence=0.8, grayscale=True)
    normal_stage_coordinate = pyautogui.center(normal_stage)
    pyautogui.moveTo(normal_stage_coordinate, duration=0.2)  # 合戰場
    pyautogui.click()
    time.sleep(0.5)
    if Chapter == '一':
        Chapter_1 = pyautogui.locateOnScreen(r'button\Chapter_1.PNG', confidence=0.8, grayscale=True)
        Chapter_coordinate = pyautogui.center(Chapter_1)
    elif Chapter == '二':
        Chapter_2 = pyautogui.locateOnScreen(r'button\Chapter_2.PNG', confidence=0.8, grayscale=True)
        Chapter_coordinate = pyautogui.center(Chapter_2)
    elif Chapter == '三':
        Chapter_3 = pyautogui.locateOnScreen(r'button\Chapter_3.PNG', confidence=0.8, grayscale=True)
        Chapter_coordinate = pyautogui.center(Chapter_3)
    elif Chapter == '四':
        Chapter_4 = pyautogui.locateOnScreen(r'button\Chapter_4.PNG', confidence=0.8, grayscale=True)
        Chapter_coordinate = pyautogui.center(Chapter_4)
    elif Chapter == '五':
        Chapter_5 = pyautogui.locateOnScreen(r'button\Chapter_5.PNG', confidence=0.8, grayscale=True)
        Chapter_coordinate = pyautogui.center(Chapter_5)
    elif Chapter == '六':
        Chapter_6 = pyautogui.locateOnScreen(r'button\Chapter_6.PNG', confidence=0.8, grayscale=True)
        Chapter_coordinate = pyautogui.center(Chapter_6)
    elif Chapter == '七':
        Chapter_7 = pyautogui.locateOnScreen(r'button\Chapter_7.PNG', confidence=0.8, grayscale=True)
        Chapter_coordinate = pyautogui.center(Chapter_7)
    elif Chapter == '八':
        Chapter_8 = pyautogui.locateOnScreen(r'button\Chapter_8.PNG', confidence=0.8, grayscale=True)
        Chapter_coordinate = pyautogui.center(Chapter_8)
    pyautogui.moveTo(Chapter_coordinate,duration=0.2)
    pyautogui.click()
    decide = pyautogui.locateOnScreen(r'button\004.PNG', confidence=0.8, grayscale=True)
    decide_coordinate = pyautogui.center(decide)
    pyautogui.moveTo(decide_coordinate, duration=0.2)    # 決定
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

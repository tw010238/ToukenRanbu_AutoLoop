import pyautogui
import time

# time.sleep(2)
# mouse_pos = pyautogui.position()
# print(mouse_pos)


# 目錄 > 出陣 > 第五章 > 決定 > 第四節 > 部隊選擇 > 部隊三(太刀) >　出陣
def start_the_battle(Chapter,field,team):
    index = pyautogui.locateOnScreen(r'button\001.PNG', confidence=0.9, grayscale=True)
    index_coordinate = pyautogui.center(index)
    pyautogui.moveTo(index_coordinate,duration=0.2)    # 點擊目錄
    pyautogui.click()
    time.sleep(1)
    index_start = pyautogui.locateOnScreen(r'button\index_start.PNG', confidence=0.9, grayscale=True)
    index_start_coordinate = pyautogui.center(index_start)
    pyautogui.moveTo(index_start_coordinate, duration=0.2)    # 點擊目錄的出陣
    pyautogui.click()

    # 選擇章節
    while True:    # 等畫面出來再繼續，以return鍵為準
        time.sleep(1)
        try:
            pyautogui.locateOnScreen(r'button\return.png', confidence=0.9, grayscale=True)
            time.sleep(1)
            break
        except:
            continue
    normal_stage = pyautogui.locateOnScreen(r'button\normal_stage.PNG', confidence=0.9, grayscale=True)
    normal_stage_coordinate = pyautogui.center(normal_stage)
    pyautogui.moveTo(normal_stage_coordinate, duration=0.2)  # 合戰場
    pyautogui.click()
    time.sleep(0.5)
    if Chapter == '一':
        Chapter_1 = pyautogui.locateOnScreen(r'button\Chapter_1.PNG', confidence=0.9, grayscale=True)
        Chapter_coordinate = pyautogui.center(Chapter_1)
    elif Chapter == '二':
        Chapter_2 = pyautogui.locateOnScreen(r'button\Chapter_2.PNG', confidence=0.9, grayscale=True)
        Chapter_coordinate = pyautogui.center(Chapter_2)
    elif Chapter == '三':
        Chapter_3 = pyautogui.locateOnScreen(r'button\Chapter_3.PNG', confidence=0.9, grayscale=True)
        Chapter_coordinate = pyautogui.center(Chapter_3)
    elif Chapter == '四':
        Chapter_4 = pyautogui.locateOnScreen(r'button\Chapter_4.PNG', confidence=0.9, grayscale=True)
        Chapter_coordinate = pyautogui.center(Chapter_4)
    elif Chapter == '五':
        Chapter_5 = pyautogui.locateOnScreen(r'button\Chapter_5.PNG', confidence=0.9, grayscale=True)
        Chapter_coordinate = pyautogui.center(Chapter_5)
    elif Chapter == '六':
        Chapter_6 = pyautogui.locateOnScreen(r'button\Chapter_6.PNG', confidence=0.9, grayscale=True)
        Chapter_coordinate = pyautogui.center(Chapter_6)
    elif Chapter == '七':
        Chapter_7 = pyautogui.locateOnScreen(r'button\Chapter_7.PNG', confidence=0.9, grayscale=True)
        Chapter_coordinate = pyautogui.center(Chapter_7)
    elif Chapter == '八':
        Chapter_8 = pyautogui.locateOnScreen(r'button\Chapter_8.PNG', confidence=0.9, grayscale=True)
        Chapter_coordinate = pyautogui.center(Chapter_8)
    pyautogui.moveTo(Chapter_coordinate,duration=0.2)
    pyautogui.click()
    decide = pyautogui.locateOnScreen(r'button\004.PNG', confidence=0.9, grayscale=True)
    decide_coordinate = pyautogui.center(decide)
    pyautogui.moveTo(decide_coordinate, duration=0.2)    # 決定
    pyautogui.click()
    time.sleep(0.5)

    # 選擇地區
    if field == '一':
        scene_1 = pyautogui.locateOnScreen(r'button\scene_1.PNG', confidence=0.9, grayscale=True)
        scene_coordinate = pyautogui.center(scene_1)
    elif field == '二':
        scene_2 = pyautogui.locateOnScreen(r'button\scene_2.PNG', confidence=0.9, grayscale=True)
        scene_coordinate = pyautogui.center(scene_2)
    elif field == '三':
        scene_3 = pyautogui.locateOnScreen(r'button\scene_3.PNG', confidence=0.9, grayscale=True)
        scene_coordinate = pyautogui.center(scene_3)
    elif field == '四':
        scene_4 = pyautogui.locateOnScreen(r'button\scene_4.PNG', confidence=0.9, grayscale=True)
        scene_coordinate = pyautogui.center(scene_4)
    pyautogui.moveTo(scene_coordinate, duration=0.2)
    pyautogui.click()

    # 部隊選擇按鍵
    choose_team = pyautogui.locateOnScreen(r'button\choose_team.PNG', confidence=0.9, grayscale=True)
    choose_team_coordinate = pyautogui.center(choose_team)
    pyautogui.moveTo(choose_team_coordinate, duration=0.2)
    pyautogui.click()
    time.sleep(0.5)

    # 部隊選擇
    if team == '一':
        team_1 = pyautogui.locateOnScreen(r'button\team_1.PNG', confidence=0.9, grayscale=True)
        team_coordinate = pyautogui.center(team_1)
    elif team == '二':
        team_2 = pyautogui.locateOnScreen(r'button\team_2.PNG', confidence=0.9, grayscale=True)
        team_coordinate = pyautogui.center(team_2)
    elif team == '三':
        team_3 = pyautogui.locateOnScreen(r'button\team_3.PNG', confidence=0.9, grayscale=True)
        team_coordinate = pyautogui.center(team_3)
    elif team == '四':
        team_4 = pyautogui.locateOnScreen(r'button\team_4.PNG', confidence=0.9, grayscale=True)
        team_coordinate = pyautogui.center(team_4)
    elif team == '五':
        team_5 = pyautogui.locateOnScreen(r'button\team_5.PNG', confidence=0.9, grayscale=True)
        team_coordinate = pyautogui.center(team_5)
    pyautogui.moveTo(team_coordinate, duration=0.2)
    pyautogui.click()
    pyautogui.moveTo(1570,920,duration=0.2)    # 出陣
    # pyautogui.click()


# 下一關
def next_stage():
    while True:
        try:
            pyautogui.locateOnScreen(r'button\warnning1.PNG',confidence=0.9, grayscale = True)        # 出現重傷警告時退出。不知道為甚麼，這張圖在螢幕上找不太到，所以要調低信心度
            break
        except:
            try:
                next_button = pyautogui.locateOnScreen(r'button\next_stage.PNG',confidence=0.9, grayscale = True)
                next_button_center = pyautogui.center(next_button)
                pyautogui.moveTo(next_button_center,duration=0.2)
                pyautogui.click()
            except:
                try:
                    pyautogui.locateOnScreen(r'button\home.PNG',confidence=0.9, grayscale = True)
                    break
                except:
                    try:
                        formation = pyautogui.locateOnScreen(r'button\formation.PNG',confidence=0.9, grayscale = True)
                        formation_center = pyautogui.center(formation)
                        pyautogui.moveTo(formation_center, duration=0.2)
                        pyautogui.click()
                    except:
                        try:
                            pyautogui.locateOnScreen(r'button\DMM GAMES.PNG',confidence=0.9, grayscale = True)
                            pyautogui.moveTo(266, 994, 0.2)
                            pyautogui.click()
                            time.sleep(0.8)
                        except:
                            break

def loop(Chapter,field,team):
    start_the_battle(Chapter,field,team)
    next_stage()



# 測試行

# time.sleep(2)
# start_the_battle("四","四","四")
import pyautogui
import time



# 目錄 > 出陣 > 第五章 > 決定 > 第四節 > 部隊選擇 > 部隊三(太刀) >　出陣
# 改成
# 目錄 > 出陣 > 等待 > 催物 > 難度 > 部隊選擇 > 隊伍 > 出陣
def start_the_battle(difficulty,auto_replenish,team):      #replenish = refill
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
        try:
            pyautogui.locateOnScreen(r'button\return.png', confidence=0.9, grayscale=True)
            time.sleep(1)
            break
        except:
            continue
    ERS_stage = pyautogui.locateOnScreen(r'button\event_stage.PNG', confidence=0.9, grayscale=True)
    ERS_stage_coordinate = pyautogui.center(ERS_stage)
    pyautogui.moveTo(ERS_stage_coordinate, duration=0.2)  # 催物
    pyautogui.click()
    time.sleep(0.5)
    if difficulty == '難易度‧易':
        difficulty_1 = pyautogui.locateOnScreen(r'button\easy_mode.PNG', confidence=0.9, grayscale=True)
        difficulty_coordinate = pyautogui.center(difficulty_1)
    elif difficulty == '難易度‧普':
        difficulty_2 = pyautogui.locateOnScreen(r'button\normal_mode.PNG', confidence=0.9, grayscale=True)
        difficulty_coordinate = pyautogui.center(difficulty_2)
    elif difficulty == '難易度‧難':
        difficulty_3 = pyautogui.locateOnScreen(r'button\hard_mode.PNG', confidence=0.9, grayscale=True)
        difficulty_coordinate = pyautogui.center(difficulty_3)
    elif difficulty == '難易度‧超難':
        difficulty_4 = pyautogui.locateOnScreen(r'button\super_mode.PNG', confidence=0.9, grayscale=True)
        difficulty_coordinate = pyautogui.center(difficulty_4)

    pyautogui.moveTo(difficulty_coordinate,duration=0.2)
    pyautogui.click()
    choose_team = pyautogui.locateOnScreen(r'button\choose_team.PNG', confidence=0.9, grayscale=True)
    choose_team_coordinate = pyautogui.center(choose_team)
    pyautogui.moveTo(choose_team_coordinate, duration=0.2)    # 部隊選擇
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
# 微改
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

# 多一個特別關卡



# 要加特別關卡判斷
def loop(difficulty,field,team):
    start_the_battle(difficulty,field,team)
    next_stage()



# 測試行
# time.sleep(2)
# start_the_battle('難易度‧難','全部補充','四')
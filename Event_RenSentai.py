import pyautogui
import time
from tool.click_button import click_button



# 目錄 > 出陣 > 第五章 > 決定 > 第四節 > 部隊選擇 > 部隊三(太刀) >　出陣
# 改成
# 目錄 > 出陣 > 等待 > 催物 > 難度 > 部隊選擇 > 隊伍 > 出陣
def start_the_battle(difficulty,auto_replenish,team):      #replenish = refill
    click_button(r'button\001.PNG')
    time.sleep(1)
    click_button(r'button\index_start.PNG')    # 點擊目錄的出陣

    # 選擇章節
    while True:    # 等畫面出來再繼續，以return鍵為準
        try:
            pyautogui.locateOnScreen(r'button\return.png', confidence=0.9, grayscale=True)
            time.sleep(1)
            break
        except:
            continue
    click_button(r'button\event_stage.PNG')
    time.sleep(1.5)
    if difficulty == '難易度‧易':
        click_button(r'button\ERS\easy_mode.PNG')
    elif difficulty == '難易度‧普':
        click_button(r'button\ERS\normal_mode.PNG')
    elif difficulty == '難易度‧難':
        click_button(r'button\ERS\hard_mode.PNG')
    elif difficulty == '難易度‧超難':
        click_button(r'button\ERS\super_mode.PNG')
    click_button(r'button\choose_team.PNG')    # 部隊選擇
    time.sleep(0.5)


    # 部隊選擇
    if team == '一':
        click_button(r'button\team_1.PNG')
    elif team == '二':
        click_button(r'button\team_2.PNG')
    elif team == '三':
        click_button(r'button\team_3.PNG')
    elif team == '四':
        click_button(r'button\team_4.PNG')
    elif team == '五':
        click_button(r'button\team_5.PNG')
    click_button(r'button\008.PNG')  # 出陣
    time.sleep(1)
    while True:
        try:
            click_button(r'button\ERS\decide.PNG')
            return 'start'
        except:
            if auto_replenish == '不補充':
                return 'stop'
            else:
                click_button(r'button\ERS\replenish.PNG')
                time.sleep(0.3)
                if auto_replenish == '單個補充':
                    click_button(r'button\ERS\replenish_1.PNG')
                elif auto_replenish == '三個補充':
                    click_button(r'button\ERS\replenish_3.PNG')
                elif auto_replenish == '全部補充':
                    click_button(r'button\ERS\full_replenish.PNG')
                time.sleep(0.5)
                click_button(r'button\yes.PNG')
                time.sleep(0.5)
                click_button(r'button\close.PNG')
                time.sleep(0.5)
                click_button(r'button\008.PNG')  # 出陣
                time.sleep(0.5)



# 下一關
# 微改
def next_stage():
    while True:
        try:    # 重傷警告 退出
            pyautogui.locateOnScreen(r'button\warnning1.PNG',confidence=0.9, grayscale = True)        # 出現重傷警告時退出。不知道為甚麼，這張圖在螢幕上找不太到，所以要調低信心度
            break
        except:
            try:    # 行軍按鍵出現 下一關
                click_button(r'button\ERS\continue.PNG')
            except:
                try:    # 沒回到丸本的狀況
                    pyautogui.locateOnScreen(r'button\choose_team.PNG', confidence=0.9, grayscale=True)
                    time.sleep(3)
                    break
                except:
                    try:    # 丸本圖案出現 結束
                        pyautogui.locateOnScreen(r'button\home.PNG',confidence=0.9, grayscale = True)
                        break
                    except:
                        try:    # 索敵失敗
                            click_button(r'button\formation.PNG')
                        except:
                            try:    # 中斷LOOP
                                pyautogui.locateOnScreen(r'button\DMM GAMES.PNG',confidence=0.9, grayscale = True)
                                pyautogui.moveTo(266, 994, 0.2)
                                pyautogui.click()
                                time.sleep(0.5)
                            except:
                                break

# # 特別關卡
# def special(difficulty,team):
#     if difficulty == '難易度‧易':
#         difficulty_1 = pyautogui.locateOnScreen(r'button\ERS\easy_mode.PNG', confidence=0.9, grayscale=True)
#         difficulty_coordinate = pyautogui.center(difficulty_1)
#     elif difficulty == '難易度‧普':
#         difficulty_2 = pyautogui.locateOnScreen(r'button\ERS\normal_mode.PNG', confidence=0.9, grayscale=True)
#         difficulty_coordinate = pyautogui.center(difficulty_2)
#     elif difficulty == '難易度‧難':
#         difficulty_3 = pyautogui.locateOnScreen(r'button\ERS\hard_mode.PNG', confidence=0.9, grayscale=True)
#         difficulty_coordinate = pyautogui.center(difficulty_3)
#     elif difficulty == '難易度‧超難':
#         difficulty_4 = pyautogui.locateOnScreen(r'button\ERS\super_mode.PNG', confidence=0.9, grayscale=True)
#         difficulty_coordinate = pyautogui.center(difficulty_4)
#
#     pyautogui.moveTo(difficulty_coordinate,duration=0.2)
#     pyautogui.click()
#     choose_team = pyautogui.locateOnScreen(r'button\choose_team.PNG', confidence=0.9, grayscale=True)
#     choose_team_coordinate = pyautogui.center(choose_team)
#     pyautogui.moveTo(choose_team_coordinate, duration=0.2)    # 部隊選擇
#     pyautogui.click()
#     time.sleep(0.5)
#
#     # 部隊選擇
#     if team == '一':
#         team_1 = pyautogui.locateOnScreen(r'button\team_1.PNG', confidence=0.9, grayscale=True)
#         team_coordinate = pyautogui.center(team_1)
#     elif team == '二':
#         team_2 = pyautogui.locateOnScreen(r'button\team_2.PNG', confidence=0.9, grayscale=True)
#         team_coordinate = pyautogui.center(team_2)
#     elif team == '三':
#         team_3 = pyautogui.locateOnScreen(r'button\team_3.PNG', confidence=0.9, grayscale=True)
#         team_coordinate = pyautogui.center(team_3)
#     elif team == '四':
#         team_4 = pyautogui.locateOnScreen(r'button\team_4.PNG', confidence=0.9, grayscale=True)
#         team_coordinate = pyautogui.center(team_4)
#     elif team == '五':
#         team_5 = pyautogui.locateOnScreen(r'button\team_5.PNG', confidence=0.9, grayscale=True)
#         team_coordinate = pyautogui.center(team_5)
#     pyautogui.moveTo(team_coordinate, duration=0.2)
#     pyautogui.click()
#     start_button = pyautogui.locateOnScreen(r'button\008.PNG', confidence=0.9, grayscale=True)
#     start_button_coordinate = pyautogui.center(start_button)
#     pyautogui.moveTo(start_button_coordinate, duration=0.2)  # 出陣
#     pyautogui.click()
#     time.sleep(0.5)
#     decide = pyautogui.locateOnScreen(r'button\ERS\decide.PNG', confidence=0.9, grayscale=True)
#     decide_coordinate = pyautogui.center(decide)
#     pyautogui.moveTo(decide_coordinate, duration=0.2)
#     pyautogui.click()


def ERS_loop(difficulty,field,team):
    S_T = start_the_battle(difficulty,field,team)
    if S_T == 'start':
        next_stage()
        return 'keep'
    else:
        return 'stop'
    # try:
    #     pyautogui.locateOnScreen(r'button\ERS\special.PNG', confidence=0.9, grayscale=True)
    #     special(difficulty,team)
    #     next_stage()
    # except:
    #     pass



# # 測試行
# time.sleep(2)
# ERS_loop('難易度‧超難','全部補充','一')
# # start_the_battle('難易度‧難','全部補充','四')
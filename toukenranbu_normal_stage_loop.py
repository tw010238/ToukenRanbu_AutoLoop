import pyautogui
import time
from tool.click_button import click_button

# time.sleep(2)
# mouse_pos = pyautogui.position()
# print(mouse_pos)


# 目錄 > 出陣 > 第五章 > 決定 > 第四節 > 部隊選擇 > 部隊三(太刀) >　出陣
def start_the_battle(Chapter,field,team):
    click_button(r'button\001.PNG')    # 點擊目錄
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
    click_button(r'button\normal_stage.PNG')  # 合戰場
    time.sleep(0.5)
    if Chapter == '一':
        click_button(r'button\Chapter_1.PNG')
    elif Chapter == '二':
        click_button(r'button\Chapter_2.PNG')
    elif Chapter == '三':
        click_button(r'button\Chapter_3.PNG')
    elif Chapter == '四':
        click_button(r'button\Chapter_4.PNG')
    elif Chapter == '五':
        click_button(r'button\Chapter_5.PNG')
    elif Chapter == '六':
        click_button(r'button\Chapter_6.PNG')
    elif Chapter == '七':
        click_button(r'button\Chapter_7.PNG')
    elif Chapter == '八':
        click_button(r'button\Chapter_8.PNG')
    click_button(r'button\004.PNG')    # 決定
    time.sleep(0.5)

    # 選擇地區
    if field == '一':
        click_button(r'button\scene_1.PNG')
    elif field == '二':
        click_button(r'button\scene_2.PNG')
    elif field == '三':
        click_button(r'button\scene_3.PNG')
    elif field == '四':
        click_button(r'button\scene_4.PNG')

    # 部隊選擇按鍵
    click_button(r'button\choose_team.PNG')
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


# 下一關
def next_stage():
    while True:
        try:        # 重傷警告
            pyautogui.locateOnScreen(r'button\warnning1.PNG',confidence=0.9, grayscale = True)        # 出現重傷警告時退出。不知道為甚麼，這張圖在螢幕上找不太到，所以要調低信心度
            break
        except:
            try:        # 繼續行軍
                click_button(r'button\next_stage.PNG')
            except:
                try:        # 回到丸本
                    pyautogui.locateOnScreen(r'button\home.PNG',confidence=0.9, grayscale = True)
                    break
                except:
                    try:        # 索敵失敗 - 方陣
                        click_button(r'button\formation.PNG')
                    except:
                        try:        # 一直點左下
                            pyautogui.locateOnScreen(r'button\DMM GAMES.PNG',confidence=0.9, grayscale = True)
                            pyautogui.moveTo(266, 994, 0.2)
                            pyautogui.click()
                            time.sleep(0.5)
                        except:        # DMM消失，終止程式
                            break

def loop(Chapter,field,team):
    start_the_battle(Chapter,field,team)
    next_stage()



# 測試行

# time.sleep(2)
# start_the_battle("四","四","四")
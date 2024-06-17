import pyautogui
import time

# for i in range(8):
time.sleep(2)
# mouse_pos = pyautogui.position()
# print(mouse_pos)
# time.sleep(2)
#
# coordinate = [(517, 643),(598, 767),(709, 663),(829, 792),(945, 644),(1059, 771),(1187, 662),(777,987)]
# for x,y in coordinate:
#     pyautogui.moveTo(x,y,duration=0.2)
#     pyautogui.click()


x = pyautogui.locateOnScreen(r'button\yes.png')
x = pyautogui.center(x)
pyautogui.moveTo(x,duration=0.2)


# 地域一  x=484, y=640
# 地域二  x=815, y=640
# 地域三  x=1142, y=640
# 地域四  x=1482, y=640



# 部隊一座標  x=406, y=335
# 部隊二座標  x=538, y=335
# 部隊三座標  x=670, y=335
# 部隊四座標  x=802, y=335
# 部隊五座標  x=934, y=335


# Point(x=517, y=645)
# Point(x=598, y=790)
# Point(x=709, y=645)
# Point(x=829, y=790)
# Point(x=945, y=645)
# Point(x=1059, y=790)
# Point(x=1187, y=645)
# Point(x=1297, y=790)
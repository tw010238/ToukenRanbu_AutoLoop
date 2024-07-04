import pyautogui


def click_button(graph_path):
    button = pyautogui.locateOnScreen(graph_path, confidence=0.9, grayscale=True)
    button_coordinate = pyautogui.center(button)
    pyautogui.moveTo(button_coordinate, duration=0.2)
    pyautogui.click()
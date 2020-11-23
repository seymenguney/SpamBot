import pyautogui
import webbrowser as wb
import time
wb.open("web.whatsapp.com")
time.sleep(10)
while True:
    pyautogui.press("t")
    pyautogui.press("e")
    pyautogui.press("x")
    pyautogui.press("t")
    pyautogui.press("enter")
import time
import pyautogui
import pygetwindow as gw
import sys
from datetime import datetime

info = open('timing.txt', 'r') 
Lines = info.readlines() 
  
count = 0
# Strips the newline character 
data = []
for line in Lines: 
    print(line)
    ldata = line.split(',')
    data = ldata
print(data)


meeting_id = data[1]  #Meeting ID for testing
meeting_password = data[2] #Meeting password for testing
nickname = data[3] #Nickname while logging in
meeting_time = data[0]

def automate():
    potentialzoomwin = gw.getWindowsWithTitle('Zoom')
    for x in potentialzoomwin:
        xsize = x.size[0]
        if(xsize < 1900):
            x.minimize()
            x.restore()
            x.activate()



    time.sleep(2)
    for i in range(0,7):
        print("Pressing tab " + str(i))
        pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(meeting_id)
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.write(nickname)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.write(meeting_password)
    time.sleep(1)
    pyautogui.press('enter')
    """
    time.sleep(3)
    for i in range(0,5):
        pyautogui.press('tab')
    pyautogui.press('enter')
    """

while True:
    alreadyin = 0
    if(alreadyin == 0):
        timestamp = datetime.now().time()
        hm = str(timestamp)[:5]
    if hm == meeting_time:
        print("Meeting time!")
        alreadyin = 1
        automate()

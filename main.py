import pyautogui as ui
from PIL import ImageGrab
import time

while True:
    print("enter DDLC")
    ui.leftClick(200, 470)

    print("load menu")
    for t in range(12):
        time.sleep(1)
        print(t)

    print("grab image")
    pic = ImageGrab.grab()
    # pic.save("shortcut.jpg")

    print("exit DDLC and back to OS")
    ui.leftClick(150, 900)
    ui.leftClick(850, 600)
    time.sleep(2)

    # get pixel from characters image (actually from Monika)
    if pic.convert("RGB").getpixel((1600, 680)) != (166, 132, 143):
        break

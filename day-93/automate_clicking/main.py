import pyautogui
from PIL import Image as im
import cv2
import numpy as np
import keyboard

#instructions:
# Please open the page https://elgoog.im/t-rex/ and let it run in full screen mode.

# start the game with the help of your mouse

game = False
listen = True

while listen:
    if keyboard.is_pressed('space'):
        image = pyautogui.screenshot()
        screen_size = pyautogui.size()

        black_part = (screen_size.width/2)*0.8
        image_np = np.array(image)
        image_np[:, int(black_part):] = [0, 0, 0]

        template = cv2.imread("pictures/single_items/small_cactus.png")

        #turns template and screenshot into grey colors
        imageGray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
        templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
        location = np.unravel_index(result.argmax(), result.shape)
        data = im.fromarray(imageGray)
        # saving the final output
        # as a PNG file
        data.save('gfg_dummy_pic.png')
        game = True
        listen = False




while game:
    """The try except block is only used to by pass a bug"""
    try:
        jumper = pyautogui.pixelMatchesColor(int(location[1]), int(location[0]), (83, 83, 83))
        if jumper:
            pyautogui.press('space')

    except OSError:
        jumper = pyautogui.pixelMatchesColor(int(location[1]), int(location[0]), (83, 83, 83))
        if jumper:
            pyautogui.press('space')


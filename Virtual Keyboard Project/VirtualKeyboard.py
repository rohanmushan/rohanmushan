import cv2
import numpy as np
from pynput.keyboard import Controller
from time import sleep

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720) 
# Define the color range for tracking (e.g., skin or glove color in HSV)
lower_color = np.array([0, 48, 80], dtype=np.uint8)  # Lower bound of color
upper_color = np.array([20, 255, 255], dtype=np.uint8)  # Upper bound of color

keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
      ]

finalText = ""
keyboard = Controller()

class Button():
    def _init_(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text

buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img

while True:
    success, img = cap.read()
    if not success:
        print("Error: Failed to capture image.")
        break

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_color, upper_color)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        max_contour = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(max_contour)

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        hand_center = (x + w // 2, y + h // 2)

        cv2.circle(img, hand_center, 10, (0, 0, 255), -1)

        for button in buttonList:
            bx, by = button.pos
            bw, bh = button.size

            if bx < hand_center[0] < bx + bw and by < hand_center[1] < by + bh:

                cv2.rectangle(img, (bx - 5, by - 5), (bx + bw + 5, by + bh + 5), (175, 0, 175), cv2.FILLED)
                cv2.putText(img, button.text, (bx + 20, by + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

                if cv2.norm(hand_center, (bx + bw // 2, by + bh // 2)) < 30: 
                    if button.text == 'Backspace':
                        finalText = finalText[:-1]
                    else:
                        keyboard.press(button.text)
                        sleep(0.1)
                        keyboard.release(button.text)
                        finalText += button.text
                    sleep(0.15)

    cv2.rectangle(img, (50, 350), (700, 450), (0, 0, 0), cv2.FILLED)
    cv2.putText(img, finalText, (60, 430), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

    img = drawAll(img, buttonList)

    cv2.imshow("Virtual Keyboard", img)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

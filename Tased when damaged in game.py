from hmac import new
import numpy as np
import cv2
from PIL import ImageGrab
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from Arduino import Arduino
frame = None
Currenthealth = 100

def lost_health(img):
    global Currenthealth
    txt = pytesseract.image_to_string(img)
    health = int(txt)
    if txt == " ":
        return False
    if health < Currenthealth:
        Currenthealth = health
        print(Currenthealth)
        return True
    return False
    
def gained_health(img):
    global Currenthealth
    txt = pytesseract.image_to_string(img)
    health_gain = int(txt)
    if health_gain > Currenthealth:
        Currenthealth = health_gain
        print(Currenthealth)
        return True
    return False

while True:
    img = ImageGrab.grab(bbox=(100, 700, 700, 900)) #x, y, w, h
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0Xff == ord('q'):
        cv2.destroyAllWindows()
        break
    try:
        lost_health(frame)
        gained_health(frame)
        Currenthealth = int(pytesseract.image_to_string(frame))
    except ValueError:
        pass
    


    

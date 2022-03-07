from hmac import new
import numpy as np
import cv2
from PIL import ImageGrab
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
frame = None

while True:
    img = ImageGrab.grab(bbox=(0, 900, 1100, 1100)) #x, y, w, h
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0Xff == ord('q'):
        cv2.destroyAllWindows()
        break

txt = pytesseract.image_to_string(frame)
print(txt)

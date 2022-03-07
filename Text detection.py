import numpy as np
import cv2
from PIL import ImageGrab
import pytesseract

while True:
    img = ImageGrab.grab(bbox=(0, 1000, 1000, 1100)) #x, y, w, h
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0Xff == ord('q'):
        cv2.destroyAllWindows()
        break
    

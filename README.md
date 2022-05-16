# Programmering-1
## For projects in course Programmering 1

The code [Tased when damaged in game.py](https://github.com/samuelcool5/Programmering-1/blob/main/Tased%20when%20damaged%20in%20game.py) detects if damage has been taken in a game by reading the numbers of the health 0-100, then tases you if health goes down.

Check [Text detection.py](https://github.com/samuelcool5/Programmering-1/blob/main/Text%20detection.py) for history to a certain point then go to [Tased when damaged in game.py](https://github.com/samuelcool5/Programmering-1/blob/main/Tased%20when%20damaged%20in%20game.py) for the rest of the history and the finnished code.

## Running *Tased when damaged in game.py*

### In order to run the code a few Modules installations must be done:
1. OpenCV
   - pip install opencv-python
2. pytesseract
   - pip install pytesseract
   - Download and install [Tesseract-OCR](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.1.20220118.exe), To access tesseract-OCR from any location you may have to add the directory where the tesseract-OCR binaries are located to the Path variables, probably C:\Program Files\Tesseract-OCR.
3. PySerial
   - pip install pyserial
4. Arduino-Python3 Command API
   - pip install arduino-python3 
   - load sketch onto arduino, [MORE INFO](https://github.com/mkals/Arduino-Python3-Command-API)
### Change imageGrab box resulotion:
![imagegrab parameters](https://user-images.githubusercontent.com/97743581/161279814-f64810ad-ae20-49ec-b2d7-ba1706be73c1.jpg)

## The taser part:
![IMG_20220516_101028](https://user-images.githubusercontent.com/97743581/168549416-000924b5-8769-4eb7-b175-9fa1ae23ea10.jpg)
### Components
- Arduino Uno
- Relay
   - Gnd to Gnd
   - Vcc to 5V
   - In1 to Pin13
- Battery holder
- Taser module from Electric Fly Swatter
   - Wire to relay instead of button

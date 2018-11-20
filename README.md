# Disclaimer
This is my first python srcipt, so expect the code to be messy and not perfect
# What is this
This is a Script made with Python that play sounds when you gain or lose health in Fortnite, reading your health using OCR

Only you will hear the sounds!!

For the .exe version view releases [here](https://github.com/RKaoZ/Fortnite-Health-Sounds/releases)
# Requirements
You need Python, I recomend using the 3.6 version of [Anaconda](https://www.anaconda.com/download/), and this libraries:
```
pyscreenshot
pytesseract
Pillow
pygame
time
```
# How to use it
Play in Fullscreen in 1920x1080p resolution.

When finish intalling all the libraries navigate using the Command Prompt to the folder where you have the script and type:
```
python main.py
```
# Modifications
You can change the audio that plays when you lose or gain health. Just replace the audios with the ones you want.

**DONT CHANGE THE FOLDER OR NAME OF THE AUDIOS OR THEY WONT PLAY**
```
nice.mp3 plays when you gain healt

pium.mp3 plays when you lose health
```
# Bugs
The known bugs are:
```
- Tesseract fails to read some numbers
```

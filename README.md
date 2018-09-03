# Disclaimer
This is in a early stage, have bugs and **IT'S NOT FINISHED**

This is my first python srcipt, so expect the code to be messy and not perfect
# What is this
This is a Script made with Python that play sounds when you gain or lose health using OCR

To make others hear the sounds use a program like [Virtual Audio Cable](https://www.vb-audio.com/Cable/) to make a virtual microphone that stream the PC Audio, with that other will hear all the sounds throught the voice chat (**DONT USE THIS TO BOTHER OTHER PLAYERS**)
# Requirements
You need Python, I recomend using the 3.6 version of [Anaconda](https://www.anaconda.com/download/), and this libraries:
```
pyscreenshot
pytesseract
Pillow
pygame
time
```
# How To Use It
When finish intalling all the libraries navigate using the Command Prompt to the folder where you have the script, open the game and when you leave the bus type in the Command Prompt:
```
python main.py
```
**If the script can't read the health (when you open the map, health isn't displayed, etc) it will crash!!**
# Modifications
You can change the audio that plays when you lose or gain health. Just replace the audios whit the ones you want.

**DONT CHANGE THE FOLDER OR NAME OF THE AUDIOS OR THEY WONT PLAY AND WILL CAUSE AN ERROR AND WILL CRASH**
```
nice.mp3 plays when you gain healt

pium.mp3 plays when you lose health
```
# Bugs
The known bugs are:
```
OCR fails to read some numbers and will crash
Sometimes detects you have gain health when you have lost health
```

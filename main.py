import pyscreenshot
import pytesseract
from PIL import Image
from PIL import ImageGrab
from pygame import mixer
import time

previous = 100 #initial value of previous health

def image(): #Takes screenshot of the health, saves it and read from it
   im = ImageGrab.grab(bbox=(760, 968, 810, 990)) #makes a screnshot of the health
   im.save("health.jpg") #saves the image

   im = Image.open("health.jpg") #opens the image
   health = pytesseract.image_to_string(im) #writes the text read from image

   check(health) #jumps to check(health)

def check(health): #checks if health have a valid value to be converted to an integer
    try: #tries to convert health to an integer
        health = int(health)
        result(health)
    except ValueError: #if health cant be converted prints error and starts again from image()
        print ("Failed to read from image")
        image()

def result(health): #compares the previous health to the current one and plays sound
  global previous #calls the variable previous
  print ("Health=", health)
  if health < previous: #checks if the health is lower than your previous health
   print("HIT")
   mixer.init() #initialeizes mixer
   mixer.music.load("pium.mp3") #loads the audio file
   mixer.music.play() #plays the audio file
   previous = health #updates the previous health
   print("Previous Health=", previous) #prints your previous health

  if health > previous: #checks if the health is higher than your previous health
    print("NICE")
    mixer.init() #initialeizes mixer
    mixer.music.load("nice.mp3") #loads the audio file
    mixer.music.play() #plays the audio file
    previous = health #updates the previous health
    print("Previous Health=", previous) #prints your previous health
  else: 
   previous = health #updates the previous health
   print("Previous Health=", previous) #prints your previous health

while True: #repeats the code if true
    time.sleep(1) #cooldown in seconds
    image() #starts from image() again

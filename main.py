import pyscreenshot
import pytesseract
from PIL import Image
from PIL import ImageGrab
from pygame import mixer
import time

class Accumulator(object):
    none = None
    def also(self, condition):
        self.none = not condition and (self.none is None or self.none)
        return condition

previous = 100 #initial value of previous health

def start(): #here starts
 acc = Accumulator()
 also = acc.also

 if also(__name__ == '__main__'):
  x = 760
  y = 968

  offx = 50
  offy = 22
    
  im=ImageGrab.grab(bbox=(x, y, x + offx, y + offy)) #makes a screnshot of the health
  im.save("health.jpg") #saves the image

  im = Image.open("health.jpg") #opens the image
  text = int(pytesseract.image_to_string(im))

  print ("Health=", text) #prints the health
 
  global previous #calls the variable previous
  if text < previous: #checks if the health is lower than your previous health
   print("HIT")
   mixer.init() #initialeizes mixer
   mixer.music.load("pium.mp3") #loads the audio file
   mixer.music.play() #plays the audio file
   previous = text #updates the previous health
   print("Previous Health=", previous) #prints your previous health

  if text > previous: #checks if the health is higher than your previous health
    print("NICE")
    mixer.init() #initialeizes mixer
    mixer.music.load("nice.mp3") #loads the audio file
    mixer.music.play() #plays the audio file
    previous = text #updates the previous health
    print("Previous Health=", previous) #prints your previous health
  else: #
   previous = text #updates the previous health
   print("Previous Health=", previous) #prints your previous health

while True:
  time.sleep(0.5) #Loop cooldown in seconds
  start() #restarts from start
import os
os.chdir('/Users/Assignment3/images')

from PIL import Image
from simpleimage import SimpleImage

def redscreen(main_filename): 
  INTENSITY_THRESHOLD=1.05
  image=SimpleImage(main_filename)

  for pixel in image:
    average=(pixel.red + pixel.green + pixel.blue)//3
    if (pixel.red >= average*INTENSITY_THRESHOLD):
      pixel.red=255
      pixel.green=0
      pixel.blue=0
    else:
      pixel.red=average
      pixel.green=average
      pixel.blue=average    
  
  return image


def main():
  redimage=redscreen('greenland-fire.png')  
  redimage.show()

main()
import os  #to get all file names under the directory
import sys #to read arguement when execute python

from PIL import Image
from simpleimage import SimpleImage

def distance(pixel1,pixel2,pixel3):
    average_red = (pixel1.red + pixel2.red + pixel3.red) // 3
    average_green = (pixel1.green + pixel2.green + pixel3.green) // 3
    average_blue = (pixel1.blue + pixel2.blue + pixel3.blue) // 3 

    dist1 = (pixel1.red - average_red)**2 + (pixel1.green - average_green)**2 + (pixel1.blue - average_blue)**2
    dist2 = (pixel2.red - average_red)**2 + (pixel2.green - average_green)**2 + (pixel2.blue - average_blue)**2
    dist3 = (pixel3.red - average_red)**2 + (pixel3.green - average_green)**2 + (pixel3.blue - average_blue)**2

    if (dist1==min(dist1,dist2,dist3)): 
        return 1
    elif (dist2==min(dist1,dist2,dist3)): 
        return 2
    elif (dist3==min(dist1,dist2,dist3)): 
        return 3


def ghost(folder_name): 
    #Concatenate the path
    image_file_path = '/Users/Assignment3/'+folder_name
    print(image_file_path)
    files = os.listdir(image_file_path)
    print(files)
    i=1
    for file in files:
        print(file)
        globals()['image%s' % i]=SimpleImage(image_file_path+"/"+file)
        i+=1

    for y in range(image1.height):    # loop over all the rows
        for x in range(image1.width): # loop over all the columns
            image_pixel1 = image1.get_pixel(x, y)
            image_pixel2 = image2.get_pixel(x, y)
            image_pixel3 = image3.get_pixel(x, y)
            near = distance(image_pixel1,image_pixel2,image_pixel3)

            if (near==1): 
                pixel = image_pixel1
            elif (near==2):
                pixel = image_pixel2
            elif (near==3):
                pixel = image_pixel3

            image1.set_pixel(x, y, pixel)
    return image1


def main(arg1):
  ghostimage=ghost(arg1)  
  ghostimage.show()

if __name__ == "__main__":
    main(sys.argv[1])
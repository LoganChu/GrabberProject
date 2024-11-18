import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image

def flip(image_file):
    #image_rgb = read_this(image_file=image_file, gray_scale=gray_scale)
    image = Image.open(image_file)

    #Flip the across vertical axis
    horizontal_flip = image.transpose(Image.FLIP_LEFT_RIGHT)

    # Flip the across horizantal axis
    vertical_flip = image.transpose(Image.FLIP_TOP_BOTTOM)

    #vertical_flip.save("VerticalFlip.png")
    #horizontal_flip.save("HorizantalFlip.png")
    horizontal_flip.rotate(180).save("rotatedImage.png")


flip("./IntImageAndor/image_python_1.bmp")
import scipy
import tifffile
import matplotlib.pyplot as plt

def roi(image,ion_number, Manhattan_distance):
    #img = tifffile.imread(image)
    plt.imshow(image, cmap="gray")  # Use "gray" for grayscale images, or remove cmap for color images
    plt.axis("off")  # Hide axes
    plt.show()


roi("./img-ion-10/img-ion-10_MMStack_Default.ome.jpg",3,3)
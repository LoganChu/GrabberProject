import scipy
import tifffile
import matplotlib.pyplot as plt
import cv2
import numpy as np
from scipy.ndimage import maximum_filter
from skimage.feature import peak_local_max


# Load the image
#img = cv2.imread("image.jpg")

# Convert BGR (default OpenCV format) to RGB
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def roi(image,ion_number, Manhattan_distance):
    img = tifffile.imread(image)
    print(img.shape)
    print(img.dtype)

    # Crop the image (ROI)
    cropped_img = img[240:260,250:290]  # Slicing: img[y1:y2, x1:x2]

    #Corresponds to a sigma of 0.8
    blur_ksize = 3
    
    blurred_img = cv2.GaussianBlur(cropped_img, (blur_ksize, blur_ksize), 0)

    # Detect local maxima using skimage's peak_local_max
    maxima = peak_local_max(blurred_img, num_peaks=ion_number, min_distance=Manhattan_distance)

    # Plot results
    fig, ax = plt.subplots(3, 1, figsize=(12, 6))

    #Gaussian Blur Plot
    ax[0].imshow(blurred_img, cmap="gray")
    ax[0].set_title("Gaussian Blurred Image")
    ax[0].axis("off")

    #Maxima Plot
    ax[1].imshow((cropped_img), cmap="gray")
    ax[1].scatter(maxima[:, 1], maxima[:, 0], color='red', s=20, label=f"Top {ion_number} Maxima")
    ax[1].set_title(f"Top {ion_number} Maxima")
    ax[1].axis("off")

    #Bounding Boxes
    for y, x in maxima:
        cv2.rectangle(
            cropped_img, 
            (x - Manhattan_distance, y - Manhattan_distance),  # Top-left corner
            (x + Manhattan_distance, y + Manhattan_distance),  # Bottom-right corner
            (0, 0, 255),  # Blue box (BGR format)
            1  # Thickness
        )

    ax[2].imshow((cropped_img), cmap="gray")
    ax[2].set_title(f"Bounding Boxes")
    ax[2].axis("off")
    
    plt.show()

roi("./6-ion-chain/6-ion-chain_MMStack_Default.ome.tif",6,3)

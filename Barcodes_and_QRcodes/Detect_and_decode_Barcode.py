import os
import cv2
from pyzbar.pyzbar import decode
import numpy as np
import requests
import matplotlib.pyplot as plt

#Reading input bar image

filepath = 'Example_Barcode.png'
inputImage = cv2.imread(filepath)
img = inputImage.copy()

cv2.imshow('Barcode Image', inputImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

#function to display the output

# Function for displaying the rectangle over the bar code
def display(img, det_bar):
    for bar in det_bar:
        x, y, w, h = bar.rect #(x,y)of the lefthand upper cornor of rectangle and w for width, h for height
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 4)
        print(bar.data)
        print(bar.type)

    # Return results
    return img


#running the decoder function on bar image

detected_bar_codes = decode(inputImage)

#display results

if detected_bar_codes:
    bbox_img = display(img, detected_bar_codes)
    plt.imshow(bbox_img[...,::-1])
    plt.show(block=False)

else:
    print("Barcode not detected")
    plt.imshow(inputImage)

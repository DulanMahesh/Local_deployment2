import os
import cv2
import numpy as np
import time
import requests
import matplotlib.pyplot as plt

# Display the input image
filepath = 'QRcode.png'
inputImage = cv2.imread(filepath)
plt.imshow(inputImage)
plt.show(block=True)  # Block the execution until the image window is closed

# Function to display the output with a rectangle around the detected QR code
def display(im, bbox):
    # Extract corner points of the bounding box of the QR code
    pt1 = tuple(int(i) for i in bbox[0][0])  # Top-left corner of the bounding box
    pt2 = tuple(int(i) for i in bbox[0][2])  # Bottom-right corner of the bounding box
    # Draw a rectangle around the detected QR code on the image
    cv2.rectangle(im, pt1, pt2, (255, 0, 0), 3)  #  rectangle with thickness of 3

    # Display the image with the QR code highlighted
    plt.imshow(im[...,::-1])  # Convert BGR  to RGB for correct display in Matplotlib
    plt.show()

# QR code detection part

# Create a QRCodeDetector object to detect and decode the QR code
qrDecoder = cv2.QRCodeDetector()

# Detect and decode the QR code
t = time.time()  # Capture the current time to measure how long detection/decoding takes
# 'data' contains the decoded data (if any), 'bbox' contains the bounding box coordinates,
# 'rectifiedImage' is the corrected version of the QR code image
data, bbox, rectifiedImage = qrDecoder.detectAndDecode(inputImage)

# Print how long detection and decoding took (in seconds, to 3 decimal places)
print("Time Taken for Detect and Decode : {:.3f} seconds".format(time.time() - t))

# Display the results
if len(data) > 0:  # Check if the QR code was successfully detected and decoded
    print("Decoded Data : {}".format(data))  # Print the decoded data (e.g., URL or text)
    display(inputImage, bbox)  # Display the image with the QR code highlighted

else:
    # If no QR code was detected, just display the original image
    print("QR Code not detected")
    plt.imshow(inputImage)

plt.show(block=True)

# Save the results
cv2.imwrite("QR-output.jpg", inputImage)

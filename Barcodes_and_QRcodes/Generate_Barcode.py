import cv2
import barcode
from barcode.writer import ImageWriter

import matplotlib.pyplot as plt

#Data initialization

barcode_data_dict = {"Name":"Dulan Mahesh Suraweera","Job":"Computer Vision Engineer"}

barcode_data = str(barcode_data_dict)
print("Input Data: ", barcode_data)

#specifying the bar code type
barcode_type = barcode.get_barcode_class('code128')

#results generation
barcode_obj = barcode_type(barcode_data, writer = ImageWriter())

#saving and displaying the output

# Saving the barcode as an image
barcode_file = barcode_obj.save("Example_Barcode")

plt.imshow(cv2.imread(barcode_file))
plt.show(block=False)
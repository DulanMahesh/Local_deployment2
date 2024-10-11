import qrcode
import matplotlib.pyplot as plt

#Data initiation

data ="http://www.yahoo.com"

#creating an instance of QRCode

qr = qrcode.QRCode(
    version =1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

#adding data to the instance 'qr'

qr.add_data(data)
#generating an image from the QR code instance

img =qr.make_image(fill_color ="black", back_color ="white")

#saving the image
img.save("QRCode.png")
#displayng the image
plt.imshow(img,'gray')
plt.show(block=True)


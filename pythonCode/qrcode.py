from tkinter import *
from tkinter.ttk import *
import pyqrcode
from PIL import Image, ImageTk
import os

os.chdir(os.path.dirname(__file__))


def wifiPasswordShare():
    network = str(input("Enter SSID Name: "))
    protocol = str(input("WIFI Type: "))
    pwd = str(input("WIFI Password: "))
    Hidden = str(input("Hidden Option: "))
    return network + ".png", f"WIFI:S:{network};T:{protocol};P:{pwd};H:{Hidden};"


option = str(input("Do you need to share wifi pwd[y/n]: "))
if option[0].lower() == "y":
    image_name, qr_str = wifiPasswordShare()
else:
    qr_str = str(input("Enter your Text: "))
    image_name = qr_str.split(" ")[0] + ".png"

qr_url = pyqrcode.create(qr_str)
qr_url.png(image_name, scale=8)
print("your QR Code image is Created Successfully!")


root = Tk()
root.title("QRCode")  # Title of windows form.

root.resizable(0, 0)  # fixed size
root.iconbitmap(r'qrcode.ico')
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

# Create a photoimage object of the image in the path
image1 = Image.open(image_name)

width, height = image1.size
strSize = str(width) + "x" + str(height)
root.geometry(strSize)
test = ImageTk.PhotoImage(image1)

label1 = Label(root, image=test)
label1.image = test

# Position image
label1.place(anchor=NW)
root.mainloop()

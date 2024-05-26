import os
from tkinter import *
from tkinter import messagebox
import pyqrcode
import qrcode
from PIL import ImageTk, Image
from pathlib import Path

def gen():
    ws = Toplevel()
    ws.title("QR Code Generator")
    ws.config(bg='#90EE90')
    ws.geometry('600x500')

    def generate_QR():
        global img,img1
        inputValue = entry.get("1.0", "end-1c")
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, border=2, box_size=20)
        qr.add_data(inputValue)
        qr.make(fit=True)
        img1 = qr.make_image(fill_color="black", back_color="white")
        img1.save("xy.png")

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("xy.png")
        qr1 = pyqrcode.create(inputValue)
        img = BitmapImage(data=qr1.xbm(scale=8))
        img_lbl.config(image=img)
        output.config(text="QR code of " + inputValue)

    def dQr():
        img1.save(str(os.path.join(Path.home(), "Downloads","Qrcode.png")))



    lbl = Label(ws, text="QR CODE GENERATOR", bg='#90EE90', font=('Algerian',22))
    lbl.pack()

    lbl1 = Label(ws, text="Enter message or URL", bg='#90EE90',font=('forte',16))
    lbl1.pack()

    user_input = StringVar()
    #entry = Entry( ws, textvariable=user_input, width=40)
    entry = Text( ws, height=2, width=20)
    entry.pack(padx=20)

    button = Button(ws, text="Generate_QR", width=20, command=generate_QR)
    button.pack(pady=10)


    img_lbl = Label(ws, bg='#90EE90')
    img_lbl.pack()

    output = Label(ws, text="", bg='#90EE90')
    output.pack()

    button1 = Button(ws,text="DOWNLOAD", width=15, command=dQr)

    button1.pack(pady=10)


from feedback import feed
from tkinter import *
from scanner_qr import qr_scan
from PIL import ImageTk, Image
from text import txt
import sys
from generator import gen
root = Tk()

root.title('My first GUI')
root.geometry('1500x800')
root.configure(bg='turquoise')
canvas = Canvas(root, width=1500, height=70, bg="teal")
canvas.create_text(700, 30, text=" ..QR DOCX.. ", fill="goldenrod", font='Algerian 28 bold')
canvas.pack()


################################CLOSE_BUTTON##################################
Close_button1 = PhotoImage(file=r'C:\Users\dell\PycharmProjects\QR&Detection\Images\exit.png')
close_button = Button(root, bg='teal', border='0', image=Close_button1, command=sys.exit)
close_button.place(x=20, y=2)

################################FEEDBACK_BUTTON################################

feed_button = PhotoImage(file=r'C:\Users\dell\PycharmProjects\QR&Detection\Images\feed.png')
feedback_button = Button(root, bg='teal', fg='teal', image=feed_button, command=feed)
feedback_button.place(x=1250, y=8)

################################QR_GENERATOR###########################################################

G1 = (Image.open(r'C:\Users\dell\PycharmProjects\QR&Detection\Images\G1.png'))
G1 = G1.resize((120, 120), Image.ANTIALIAS)
bgr = ImageTk.PhotoImage(G1)
label1 = Label(root, image=bgr)

image_button1 = PhotoImage(file=r'C:\Users\dell\PycharmProjects\QR&Detection\Buttons\GENERATOR.png')
button1 = Button(root, bg='turquoise', border='0', image=image_button1,command=gen)
button1.place(x=70, y=450)
label1.place(x=330, y=490)

##################################QR_SCANNER######################################

S1 = (Image.open(r'C:\Users\dell\PycharmProjects\QR&Detection\Images\S1.png'))
S1 = S1.resize((120, 120), Image.ANTIALIAS)
bgr1 = ImageTk.PhotoImage(S1)
label2 = Label(root, image=bgr1)

image_button2 = PhotoImage(file=r'C:\Users\dell\PycharmProjects\QR&Detection\Buttons\SCANNER.png')
button2 = Button(root, bg='turquoise', border='0', image=image_button2,command=qr_scan)
button2.place(x=490, y=150)
label2.place(x=750, y=190)

################################TEXT_DETECTION############################

T1 = (Image.open(r'C:\Users\dell\PycharmProjects\QR&Detection\Images\CON1.png'))
T1 = T1.resize((120, 120), Image.ANTIALIAS)
bgr3 = ImageTk.PhotoImage(T1)

label4 = Label(root, image=bgr3)
image_button4 = PhotoImage(file=r'C:\Users\dell\PycharmProjects\QR&Detection\Buttons\CONVERTER.png')
button4 = Button(root, bg='turquoise', border='0', image=image_button4, command=txt)
button4.place(x=890, y=450)
label4.place(x=1150, y=490)

root.mainloop()

from tkinter.ttk import *
from tkinter import *
from tkinter.filedialog import *
import pyperclip
from PIL import ImageTk, Image
from pyzbar.pyzbar import decode


def qr_scan():
    root = Toplevel()
    root.geometry('1080x520+100+90')
    Frm = Frame(root, width=50, height=80, highlightbackground="black", highlightthickness=4)
    Frm.pack(side=LEFT, fill=X,expand=-0.5)

    def quit():
        root.withdraw()

    def Filed():
        filename = askopenfilename(initialdir="/", title="select",
                                   filetypes=[('image', '*.jpg'), ('image', '*.jpeg'), ('image', '*.png'),
                                              ('image', '*.svg')])
        file = str(filename)
        lst.insert(END, file)

    def show(e):
        n = lst.curselection()
        fname = lst.get(n)
        print(fname)
        images = Image.open(fname)
        images = images.resize((650, 400), Image.ANTIALIAS)
        imgg = ImageTk.PhotoImage(images)
        canvas.create_image(0, 0, image=imgg, anchor=NW)
        canvas.image = imgg

    lst = Listbox(Frm, height=5)
    lst.pack(side=TOP, fill=X, expand=-0.5)
    lst.bind("<<ListboxSelect>>", show)

    canvas = Canvas(Frm, width=650, height=400, bg='azure2')
    canvas.pack(side=LEFT)

    btn1 = Button(Frm, text="Choose Image", command=Filed, width=14, height=2)
    btn1.place(x=10, y=430)

    btn2 = Button(Frm, text="Quit", command=quit, width=14, height=2)
    btn2.place(x=270, y=430)

    def detect():
        global r
        n = lst.curselection()
        w = lst.get(n)
        reader = decode(Image.open(w))
        r=reader[0].data.decode("ascii")
        print(r)
        lbl = Label(Frm, text=r, bg='#90EE90', height=6, width=31, font=('Algerian', 12))
        lbl.place(x=700, y=180)

    def copy_qr_text():
        pyperclip.copy(r)

    Output_canvas = Canvas(Frm, width=650, height=400, bg='slategray1')
    Output_canvas.pack(side='right')

    btn1 = Button(Frm, text="Scan", command=detect, width=14, height=2)
    btn1.place(x=530, y=429)

    btnc = Button(Frm, text="Copy Text/URL", command=copy_qr_text, width=14, height=2)
    btnc.place(x=790, y=329)



    lbl = Label(Frm, text="OUTPUT", bg='slategray1', font=('chiller', 42))
    lbl.place(x=790,y=100)



